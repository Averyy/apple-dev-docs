# ProximityReaderDiscovery.Content

**Framework**: ProximityReader  
**Kind**: struct

A type that represents content you can display on the current device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Content
```

#### Overview

This structure stores information the system needs to present the appropriate interface. Don’t create instances of this structure directly. Instead, fetch each instance using the [`content(for:)`](proximityreaderdiscovery/content(for:).md) method.

Pass instances of this structure to [`presentContent(_:from:)`](proximityreaderdiscovery/presentcontent(_:from:).md) to display the associated content.

## Topics

### Getting the content identifier
- [let id: String](proximityreaderdiscovery/content/id.md)
  The unique identifier of the content.
### Getting the content description
- [let description: String](proximityreaderdiscovery/content/description.md)
  The description of the content.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](proximityreaderdiscovery/content(for:).md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Topic](proximityreaderdiscovery/topic.md)
  The topics you can present to someone.
- [var contentList: [ProximityReaderDiscovery.Content]](proximityreaderdiscovery/contentlist.md)
  The content you can present for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/content)*