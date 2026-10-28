# ProximityReaderDiscovery.Content

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that represents content you can display on the current device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct Content
```

## Overview

This structure stores information the system needs to present the appropriate interface. Don’t create instances of this structure directly. Instead, fetch each instance using the [`content(for:)`](./content%28for%29.md) method.

Pass instances of this structure to [`presentContent(_:from:)`](./presentcontent%28_,from%29.md) to display the associated content.

## Topics

### Getting the content identifier
- [let id: String](./content/id.md)
  The unique identifier of the content.
### Getting the content description
- [let description: String](./content/description.md)
  The description of the content.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Fetching the content to display
- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](./content%28for%29.md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Topic](./topic.md)
  The topics you can present to someone.
- [var contentList: [ProximityReaderDiscovery.Content]](./contentlist.md)
  The content you can present for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/content)*