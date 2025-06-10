# ProximityReaderDiscovery.Topic

**Framework**: ProximityReader  
**Kind**: enum

The topics you can present to someone.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Topic
```

## Topics

### Creating a discovery object
- [case payment(ProximityReaderDiscovery.Topic.Payment)](proximityreaderdiscovery/topic/payment(_:).md)
  A topic related to accepting payments.
- [ProximityReaderDiscovery.Topic.Payment](proximityreaderdiscovery/topic/payment.md)
  The subtopics that show merchants how to accept different types of payments with  on iPhone.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](proximityreaderdiscovery/content(for:).md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Content](proximityreaderdiscovery/content.md)
  A type that represents content you can display on the current device.
- [var contentList: [ProximityReaderDiscovery.Content]](proximityreaderdiscovery/contentlist.md)
  The content you can present for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/topic)*