# canLoadObjects(ofClass:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func canLoadObjects(ofClass aClass: any NSItemProviderReading.Type) -> Bool
```

```objc
- (BOOL) canLoadObjectsOfClass:(Class<NSItemProviderReading> *) aClass;
```

#### Return Value

[`true`](../../Swift/true.md) if at least one drag item in the session can create an instance of the specified class; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `aClass`: A class conforming to the [`NSItemProviderReading`](../../Foundation/nsitemproviderreading.md) protocol.

## Default Implementations

### UIDragDropSession Implementations
- [func canLoadObjects<T>(ofClass: T.Type) -> Bool](./canloadobjects%28ofclass%29-6x43t.md)

## See Also

### Checking for drag items
- [func hasItemsConforming(toTypeIdentifiers: [String]) -> Bool](./hasitemsconforming%28totypeidentifiers%29.md)
  Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
- [var items: [UIDragItem]](./items.md)
  An array of drag items in the drag session or drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/canloadobjects(ofclass:))*