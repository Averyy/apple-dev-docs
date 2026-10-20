# hasItemsConforming(toTypeIdentifiers:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func hasItemsConforming(toTypeIdentifiers typeIdentifiers: [String]) -> Bool
```

```objc
- (BOOL) hasItemsConformingToTypeIdentifiers:(NSArray<NSString *> *) typeIdentifiers;
```

#### Return Value

[`true`](../../Swift/true.md) if a drag item in the session conforms to any UTI in the specified array; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `typeIdentifiers`: An array of uniform type identifier (UTI) strings.

## See Also

### Checking for drag items
- [func canLoadObjects(ofClass: any NSItemProviderReading.Type) -> Bool](./canloadobjects%28ofclass%29.md)
  Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [var items: [UIDragItem]](./items.md)
  An array of drag items in the drag session or drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/hasitemsconforming(totypeidentifiers:))*