# 🍏 Apple Developer Documentation Scraper

A comprehensive Python tool that scrapes and converts Apple's entire developer documentation ecosystem (340+ frameworks, 278,778 pages) into clean markdown format with local MCP server integration for semantic search.

> **Note**: This repository contains scraped documentation from Apple's developer website. All documentation content is property of Apple Inc. This tool is intended for personal use, offline access, and AI-assisted development workflows.

## 🎯 Apple JSON API

Using Apple's internal JSON API endpoints that power their own documentation navigator, it makes it possible (and relatively easy) to scrape their documentation. This approach provides extremely fast scraping with complete structured data - no HTML parsing or browser automation needed!

```
🎯 COMPLETE FRAMEWORK LIST: https://developer.apple.com/tutorials/data/documentation/technologies.json
📊 Individual Pages: https://developer.apple.com/tutorials/data/documentation/{framework}/{page}.json
```

### 🚀 ETag Support for Efficient Updates

Apple's JSON API supports HTTP ETags, enabling highly efficient incremental updates:

```bash
# First request returns an ETag
curl -I https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
# ETag: W/"399a0f24205d58c9443159732da8989a"

# Check if content changed (returns 304 Not Modified if unchanged)
curl -H 'If-None-Match: W/"399a0f24205d58c9443159732da8989a"' ...
```

After initial ETag collection, checking 237K+ documents for changes takes only ~30 minutes using HEAD requests!

## Purpose

Apple's Developer website is terrible for AI LLM's to browse and is extremely difficult to bulk add context. Unlike the Swift Language guidelines that they host open source on Github, they hide their developer guidelines behind virtualization, lazy loading, and Javascript requirements. This scraper addresses the need for offline, searchable access to Apple's developer documentation by:

- Converting Apple's documentation into clean, structured markdown files
- Organizing content for efficient semantic search via local MCP server
- Enabling natural language queries for Apple documentation
- Preserving code examples, cross-references, and platform availability information

## Technical Approach

The scraper leverages Apple's JSON API endpoints that power their documentation website:

```
Documentation URL: https://developer.apple.com/documentation/swiftui/text.json
Pair JSON API URL: https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
```

This approach provides:
- **100x faster scraping** - Direct HTTP requests instead of browser automation
- **Complete structured data** - All content, code examples, and metadata in JSON format
- **Scalable to 100,000+ pages** - Simple async HTTP requests with rate limiting
- **Generic solution** - One scraper works for ALL frameworks
- **No JavaScript rendering needed** - Pure API calls

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Interactive mode with prompts
python3 scrape.py

# Scrape all frameworks (production run)
python3 scrape.py --all --yes

# Scrape specific frameworks
python3 scrape.py --frameworks SwiftUI UIKit Foundation --yes

# Dry run to preview what will be scraped
python3 scrape.py --frameworks SwiftUI --dry-run

# Re-scrape existing frameworks (apply fixes)
python3 scripts/utilities/rescrape_existing.py --clear-hashes

# Resume interrupted scraping
python3 scrape.py --resume --yes
```

## Output Format

Documentation is saved as markdown files organized by framework:

```
documentation/
├── swiftui/
│   ├── text.md
│   ├── button.md
│   ├── view_frame(width:height:alignment:).md
│   └── declaring-a-custom-view.md
├── uikit/
│   ├── uiview.md
│   └── uiviewcontroller.md
├── metal/
│   ├── mtldevice.md
│   └── mtlcommandqueue.md
└── etc
```

Each markdown file contains:
- API name and framework
- Platform availability
- Swift/Objective-C declarations
- Detailed descriptions
- Code examples
- Cross-references with dual linking (local .md files + Apple URLs)
- Link to original Apple documentation page

## Architecture

### Project Structure

```
apple-developer-docs/
├── scrape.py                           # Main entry point
├── documentation/                      # Scraped markdown files (output)
│   ├── Accelerate/
│   ├── Accessibility/
│   ├── AdServices/
│   ├── watchkit/
│   └── etc
├── scraper/                            # Core scraping engine
│   ├── json_scraper.py                 # Apple JSON API client
│   ├── utils/markdown_converter.py     # JSON to markdown conversion
│   └── utils/hash_manager.py           # Incremental update tracking
├── scripts/utilities/                  # Utility scripts
│   ├── scrape_all_frameworks.py        # Production scraper
│   ├── framework_list_scraper.py       # Framework discovery
│   └── rescrape_existing.py            # Re-scraping tools
├── data/                               # Generated data files
│   └── complete_frameworks_list.json   # All 342 frameworks
└── tests/                              # Test suite
```

### Key Components

- **JSON Scraper** - Fetches and parses Apple's JSON API with rate limiting
- **URL Discovery** - Traverses documentation graph to find all pages  
- **Markdown Converter** - Transforms JSON to clean markdown with cross-framework links
- **Hash Manager** - Tracks content changes for efficient incremental updates
- **Concurrent Processing** - 10 parallel requests with 0.2s rate limiting

### Supported Frameworks

The scraper handles all Apple frameworks on their documentation site:

````
Accelerate
Accessibility
AccessorySetupKit
Account & Organizational Data Sharing
Account Data Transfer
Accounts
ActivityKit
AdAttributionKit
Address Book
Address Book UI
AdServices
AdSupport
Advanced Commerce API
AGL
Analytics Reports
App Clips
App Data Transfer
App Intents
App License Delivery SDK
App Store Connect API
App Store Receipts
App Store Server API
App Store Server Notifications
App Tracking Transparency
Apple Archive
Apple CryptoKit
Apple Maps Server API
Apple Music API
Apple Music Feed
Apple News
Apple Pay Merchant Token Management API
Apple Pay on the Web
Apple Pay Web Merchant Registration API
Apple Pencil
Apple Search Ads
Apple silicon
AppKit
Application Services
ARKit
Assets Library
Assignables
Audio Toolbox
Audio Unit
AudioDriverKit
Authentication Services
Automated Device Enrollment
Automatic Assessment Configuration
Automator
AVFAudio
AVFoundation
AVKit
AVRouting
Background Assets
Background Tasks
BlockStorageDeviceDriverKit
BrowserEngineCore
BrowserEngineKit
BrowserKit
Bundle Resources
CallKit
CarKey
CarPlay
CFNetwork
Cinematic
CKTool JS
ClassKit
ClassKit Catalog API
ClockKit
CloudKit
CloudKit JS
Collaboration
ColorSync
Combine
Compositor Services
Compression
ContactProvider
Contacts
Contacts UI
Core Animation
Core Audio
Core Audio Types
Core Bluetooth
Core Data
Core Foundation
Core Graphics
Core Haptics
Core HID
Core Image
Core Location
Core Media
Core Media I/O
Core MIDI
Core ML
Core Motion
Core NFC
Core Services
Core Spotlight
Core Telephony
Core Text
Core Transferable
Core Video
Core WLAN
CoreAudioKit
CoreLocationUI
Create ML
Create ML Components
CryptoTokenKit
Darwin Notify
DataDetection
DeveloperToolsSupport
Device Management
DeviceActivity
DeviceCheck
DeviceDiscoveryExtension
DeviceDiscoveryUI
Disk Arbitration
Dispatch
Distributed
dnssd
DockKit
DriverKit
Endpoint Security
Enterprise Program API
EventKit
EventKit UI
Exception Handling
Execution Policy
Exposure Notification
ExtensionFoundation
ExtensionKit
External Accessory
External Purchase Server API
FamilyControls
File Provider
File Provider UI
FinanceKit
FinanceKitUI
Finder Sync
Force Feedback
Foundation
FSKit
Game Controller
GameKit
GameplayKit
GLKit
Group Activities
GSS
HealthKit
HIDDriverKit
HomeKit
HTTP Live Streaming
hvf
Hypervisor
iAd
Image I/O
Image Playground
ImageCaptureCore
InputMethodKit
Installer JS
IOBluetooth
IOBluetooth UI
IOKit
iOS & iPadOS Release Notes
IOSurface
IOUSBHost
iTunes Library
iWork Document Exporting API
JavaScriptCore
Journaling Suggestions
Kernel
Kernel Management
Latent Semantic Mapping
LightweightCodeRequirements
Link Presentation
LiveCommunicationKit
LivePhotosKit JS
Local Authentication
Local Authentication Embedded UI
LockedCameraCapture
macOS Release Notes
MailKit
ManagedApp
ManagedAppDistribution
ManagedSettings
ManagedSettingsUI
MapKit
MapKit JS
Maps Web Snapshots
MarketplaceKit
Matter
MatterSupport
Media Accessibility
Media Library
Media Player
Media Setup
Media Toolbox
MediaExtension
Message UI
Messages
Metal
Metal Performance Shaders
Metal Performance Shaders Graph
MetalFX
MetalKit
MetricKit
MIDIDriverKit
ML Compute
Model I/O
Multipeer Connectivity
MusicKit
Natural Language
Nearby Interaction
Network
Network Extension
NetworkingDriverKit
Notary API
Notification Center
Objective-C Runtime
Observation
Open Directory
OpenGL ES
os
OSLog
PackageDescription
Paravirtualized Graphics
PassKit (Apple Pay and Wallet)
PCIDriverKit
PDFKit
PencilKit
PHASE
PhotoKit
Playground Bluetooth
Playground Support
Preference Panes
Professional Video Applications
ProximityReader
Push to Talk
PushKit
Quartz
Quick Look
Quick Look Thumbnailing
Quick Look UI
QuickTime File Format
RealityKit
RegexBuilder
ReplayKit
RoomPlan
Roster API
Safari Developer Features
Safari Release Notes
Safari Services
SafetyKit
SceneKit
Screen Saver
Screen Time
ScreenCaptureKit
Scripting Bridge
SCSIControllerDriverKit
SCSIPeripheralsDriverKit
SecureElementCredential
Security
Security Foundation
Security Interface
SensitiveContentAnalysis
SensorKit
SerialDriverKit
Service Management
ShaderGraph
Shared With You
ShazamKit
Sign in with Apple
Siri Event Suggestions Markup
SiriKit
SiriKit Cloud Media
SKAdNetwork for Web Ads
SMS and Call Reporting
Social
Sound Analysis
Spatial
Speech
SpriteKit
StoreKit
StoreKit Test
Swift
Swift Charts
Swift Playgrounds
Swift Testing
SwiftData
SwiftUI
Symbols
Synchronization
System
System Configuration
System Extensions
TabletopKit
TabularData
Technotes
ThreadNetwork
TipKit
Translation
TV Services
TVML
TVMLKit
TVMLKit JS
tvOS Release Notes
TVUIKit
UIKit
Uniform Type Identifiers
Updates
USBDriverKit
USBSerialDriverKit
User Notifications
User Notifications UI
Video Subscriber Account
Video Toolbox
Virtualization
Vision
VisionKit
visionOS
visionOS Release Notes
vmnet
Wallet Orders
Wallet Passes
Watch Connectivity
WatchKit
watchOS apps
watchOS Release Notes
WeatherKit
WeatherKit REST API
WebKit
WebKit JS
WidgetKit
WorkoutKit
Xcode
Xcode Release Notes
XcodeKit
xcselect
XCTest
XCUIAutomation
XPC
````


## Development & Testing

```bash
# Run critical tests
python3 tests/run_critical_tests.py

# Test single page scraping  
python3 tests/test_single_page.py

# Validate cross-framework links
python3 tests/test_critical_scraping.py

# Type checking
mypy scraper/
```

## Performance Metrics

- **Rate Limiting**: 0.2s between requests, 10 concurrent connections
- **Throughput**: ~300 pages/minute with full content processing
- **Memory Usage**: ~100MB for concurrent processing
- **Incremental Updates**: Hash-based change detection avoids re-scraping unchanged content

## License & Legal

**Scraper Code**: MIT License - The scraping tool itself is open source.

**Documentation Content**: All scraped documentation content is © Apple Inc. and subject to Apple's terms of use. This tool downloads publicly available documentation for personal use and development purposes. Users are responsible for complying with Apple's terms of service.

## Acknowledgments

- All documentation content is sourced from [Apple Developer Documentation](https://developer.apple.com/documentation/)
- Each markdown file includes a link back to the original Apple documentation page
- Built for local semantic search with complete data privacy