# SpotlightSearchTool.ContentDomain

**Framework**: Core Spotlight  
**Kind**: struct

A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ContentDomain
```

#### Overview

Each domain exposes a small set of fields tuned for a specific category of user content. Developers can override the default attribute mappings.

Usage:

```swift
// Default communications schema
let guide = SpotlightSearchTool.Guide(level: .focused(.communications))

// Custom document field mapping
let domain = SpotlightSearchTool.ContentDomain.Documents(
    authors: [.authorNames, SearchableItemAttribute(rawValue: "com.myapp.chef")]
)
let guide = SpotlightSearchTool.Guide(level: .focused(.documents(domain)))
```

## Topics

### Getting the audio domain
- [static var audio: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/audio-swift.type.property.md)
  Music, podcasts, voice memos, and other audio content.
- [static func audio(SpotlightSearchTool.ContentDomain.Audio) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/audio(_:).md)
  Music, podcasts, voice memos, and other audio content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Audio](spotlightsearchtool/contentdomain/audio-swift.struct.md)
  Attribute mapping for the audio domain.
### Getting the calendar domain
- [static var calendar: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/calendar-swift.type.property.md)
  Calendar events, meetings, and scheduled items.
- [static func calendar(SpotlightSearchTool.ContentDomain.Calendar) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/calendar(_:).md)
  Calendar events, meetings, and scheduled items with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Calendar](spotlightsearchtool/contentdomain/calendar-swift.struct.md)
  Attribute mapping for the calendar domain.
### Getting the communications domain
- [static var communications: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/communications-swift.type.property.md)
  Email, messaging, and other person-to-person communication.
- [static func communications(SpotlightSearchTool.ContentDomain.Communications) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/communications(_:).md)
  Email, messaging, and other person-to-person communication with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Communications](spotlightsearchtool/contentdomain/communications-swift.struct.md)
  Attribute mapping for the communications domain.
### Getting the documents domain
- [static var documents: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/documents-swift.type.property.md)
  Documents, notes, and text-heavy content.
- [static func documents(SpotlightSearchTool.ContentDomain.Documents) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/documents(_:).md)
  Documents, notes, and text-heavy content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Documents](spotlightsearchtool/contentdomain/documents-swift.struct.md)
  Attribute mapping for the documents domain.
### Getting the items domain
- [static var items: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/items-swift.type.property.md)
  Any items with title, text, and dates.
- [static func items(SpotlightSearchTool.ContentDomain.Items) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/items(_:).md)
  Any items with title, text, and dates with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Items](spotlightsearchtool/contentdomain/items-swift.struct.md)
  Attribute mapping for the items domain.
### Getting the visual media domain
- [static var visualMedia: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/visualmedia-swift.type.property.md)
  Photos, videos, and other visual content.
- [static func visualMedia(SpotlightSearchTool.ContentDomain.VisualMedia) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/visualmedia(_:).md)
  Photos, videos, and other visual content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.VisualMedia](spotlightsearchtool/contentdomain/visualmedia-swift.struct.md)
  Attribute mapping for the visual media domain.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let configuration: SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](spotlightsearchtool/guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceProfile](spotlightsearchtool/guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.FormatLevel](spotlightsearchtool/formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain)*