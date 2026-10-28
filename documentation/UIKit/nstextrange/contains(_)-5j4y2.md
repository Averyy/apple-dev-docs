# contains(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines if the text range you specify is in the current text range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func contains(_ textRange: NSTextRange) -> Bool
```

```objc
- (BOOL) containsRange:(NSTextRange *) textRange;
```

## Return Value

Returns `true` if the range you provide is in the current range; otherwise `false`.

## Parameters

- `textRange`: An [`NSTextRange`](../nstextrange.md).

## See Also

### Finding text within the text range
- [func contains(any NSTextLocation) -> Bool](./contains%28_%29-7hvi0.md)
  Determines if the text location you specify is in the current text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextrange/contains(_:)-5j4y2)*