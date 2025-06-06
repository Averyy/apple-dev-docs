# content(for:)

**Framework**: ProximityReader  
**Kind**: method

Fetches the content for the specified topic.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
final func content(for topic: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content
```

#### Return Value

The requested content, when successful.

#### Discussion

> **Note**: The method throws a [`ProximityReaderDiscovery.ContentError`](proximityreaderdiscovery/contenterror.md) if it fails to get the content.

The method throws a [`ProximityReaderDiscovery.ContentError`](proximityreaderdiscovery/contenterror.md) if it fails to get the content.

Call this method to get the content definition for the specified topic. The discovery interface uses the specified identifier to determine what to display.

## Parameters

- `topic`: The topic you want to display.

## See Also

- [ProximityReaderDiscovery.Topic](proximityreaderdiscovery/topic.md)
  The topics you can present to someone.
- [ProximityReaderDiscovery.Content](proximityreaderdiscovery/content.md)
  A type that represents content you can display on the current device.
- [var contentList: [ProximityReaderDiscovery.Content]](proximityreaderdiscovery/contentlist.md)
  The content you can present for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/content(for:))*