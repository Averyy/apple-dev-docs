# SpotlightSearchTool.ContentDomain

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

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
- [static var audio: SpotlightSearchTool.ContentDomain](./contentdomain/audio-swift.type.property.md)
  Music, podcasts, voice memos, and other audio content.
- [static func audio(SpotlightSearchTool.ContentDomain.Audio) -> SpotlightSearchTool.ContentDomain](./contentdomain/audio%28_%29.md)
  Music, podcasts, voice memos, and other audio content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Audio](./contentdomain/audio-swift.struct.md)
  Attribute mapping for the audio domain.
### Getting the calendar domain
- [static var calendar: SpotlightSearchTool.ContentDomain](./contentdomain/calendar-swift.type.property.md)
  Calendar events, meetings, and scheduled items.
- [static func calendar(SpotlightSearchTool.ContentDomain.Calendar) -> SpotlightSearchTool.ContentDomain](./contentdomain/calendar%28_%29.md)
  Calendar events, meetings, and scheduled items with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Calendar](./contentdomain/calendar-swift.struct.md)
  Attribute mapping for the calendar domain.
### Getting the communications domain
- [static var communications: SpotlightSearchTool.ContentDomain](./contentdomain/communications-swift.type.property.md)
  Email, messaging, and other person-to-person communication.
- [static func communications(SpotlightSearchTool.ContentDomain.Communications) -> SpotlightSearchTool.ContentDomain](./contentdomain/communications%28_%29.md)
  Email, messaging, and other person-to-person communication with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Communications](./contentdomain/communications-swift.struct.md)
  Attribute mapping for the communications domain.
### Getting the documents domain
- [static var documents: SpotlightSearchTool.ContentDomain](./contentdomain/documents-swift.type.property.md)
  Documents, notes, and text-heavy content.
- [static func documents(SpotlightSearchTool.ContentDomain.Documents) -> SpotlightSearchTool.ContentDomain](./contentdomain/documents%28_%29.md)
  Documents, notes, and text-heavy content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Documents](./contentdomain/documents-swift.struct.md)
  Attribute mapping for the documents domain.
### Getting the items domain
- [static var items: SpotlightSearchTool.ContentDomain](./contentdomain/items-swift.type.property.md)
  Any items with title, text, and dates.
- [static func items(SpotlightSearchTool.ContentDomain.Items) -> SpotlightSearchTool.ContentDomain](./contentdomain/items%28_%29.md)
  Any items with title, text, and dates with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.Items](./contentdomain/items-swift.struct.md)
  Attribute mapping for the items domain.
### Getting the visual media domain
- [static var visualMedia: SpotlightSearchTool.ContentDomain](./contentdomain/visualmedia-swift.type.property.md)
  Photos, videos, and other visual content.
- [static func visualMedia(SpotlightSearchTool.ContentDomain.VisualMedia) -> SpotlightSearchTool.ContentDomain](./contentdomain/visualmedia%28_%29.md)
  Photos, videos, and other visual content with custom attribute mapping.
- [SpotlightSearchTool.ContentDomain.VisualMedia](./contentdomain/visualmedia-swift.struct.md)
  Attribute mapping for the visual media domain.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the tool behavior
- [let configuration: SpotlightSearchTool.Configuration](./configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](./configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](./guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceProfile](./guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](./guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.FormatLevel](./formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain)*