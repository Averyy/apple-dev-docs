# items

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An array of drag items in the drag session or drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var items: [UIDragItem] { get }
```

#### Discussion

The drag item’s [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object doesn’t load the data for the item until the drop interaction happens. However, before the interaction happens, you can get the item’s registered type identifiers and metadata. The data is available to you only in the drop interaction delegate’s [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) method.

## See Also

- [func canLoadObjects(ofClass: any NSItemProviderReading.Type) -> Bool](uidragdropsession/canloadobjects(ofclass:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [func hasItemsConforming(toTypeIdentifiers: [String]) -> Bool](uidragdropsession/hasitemsconforming(totypeidentifiers:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/items)*