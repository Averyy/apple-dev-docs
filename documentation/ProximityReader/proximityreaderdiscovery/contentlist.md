# contentList

**Framework**: ProximityReader  
**Kind**: property

The content you can present for the current device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
final var contentList: [ProximityReaderDiscovery.Content] { get async throws }
```

#### Discussion

This property contains zero or more [`ProximityReaderDiscovery.Content`](proximityreaderdiscovery/content.md) structures, each of which corresponds to information on a supported topic. The content associated with each structure is specific to the country of the current device. The array can be empty if no content is available for the current country.

Use this list only when you need to display a topic that isn’t available in [`ProximityReaderDiscovery.Topic`](proximityreaderdiscovery/topic.md). In all other cases, use the [`content(for:)`](proximityreaderdiscovery/content(for:).md) method to fetch the topic.

Accessing this property fetches the [`ProximityReaderDiscovery.Content`](proximityreaderdiscovery/content.md) structures from the system. If the system is unable to fetch the needed information, it throws an error.

## See Also

- [func content(for: ProximityReaderDiscovery.Topic) async throws -> ProximityReaderDiscovery.Content](proximityreaderdiscovery/content(for:).md)
  Fetches the content for the specified topic.
- [ProximityReaderDiscovery.Topic](proximityreaderdiscovery/topic.md)
  The topics you can present to someone.
- [ProximityReaderDiscovery.Content](proximityreaderdiscovery/content.md)
  A type that represents content you can display on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/contentlist)*