# contains(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines if the text range you specify is in the current text range.

**Availability**:
- macOS 12.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange/contains(_:)-5j4y2)*