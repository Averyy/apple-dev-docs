# ProximityReaderDiscovery.Topic

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

The topics you can present to someone.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
enum Topic
```

## Topics

### Creating a discovery object
- [case payment(ProximityReaderDiscovery.Topic.Payment)](./topic/payment%28_%29.md)
  A topic related to accepting payments.
- [ProximityReaderDiscovery.Topic.Payment](./topic/payment.md)
  The subtopics that show merchants how to accept different types of payments with *Tap to Pay* on iPhone.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Fetching the content to display
- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](./content%28for%29.md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Content](./content.md)
  A type that represents content you can display on the current device.
- [var contentList: [ProximityReaderDiscovery.Content]](./contentlist.md)
  The content you can present for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/topic)*