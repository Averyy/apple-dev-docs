# hasItemsConforming(toTypeIdentifiers:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func hasItemsConforming(toTypeIdentifiers typeIdentifiers: [String]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if a drag item in the session conforms to any UTI in the specified array; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `typeIdentifiers`: An array of uniform type identifier (UTI) strings.

## See Also

- [func canLoadObjects(ofClass: any NSItemProviderReading.Type) -> Bool](uidragdropsession/canloadobjects(ofclass:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [var items: [UIDragItem]](uidragdropsession/items.md)
  An array of drag items in the drag session or drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/hasitemsconforming(totypeidentifiers:))*