# canLoadObjects(ofClass:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func canLoadObjects(ofClass aClass: any NSItemProviderReading.Type) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if at least one drag item in the session can create an instance of the specified class; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `aClass`: A class conforming to the   protocol.

## See Also

- [func hasItemsConforming(toTypeIdentifiers: [String]) -> Bool](uidragdropsession/hasitemsconforming(totypeidentifiers:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
- [var items: [UIDragItem]](uidragdropsession/items.md)
  An array of drag items in the drag session or drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/canloadobjects(ofclass:))*