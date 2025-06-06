# availableType(from:)

**Framework**: AppKit  
**Kind**: method

Returns from a given array of types the first type within the pasteboard item, according to the ordering of types.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func availableType(from types: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?
```

#### Return Value

The first (according to the sender’s ordering of `types`) type in `types` contained in the pasteboard item, or `nil` if the receiver does not contain any types given in `types`.

#### Discussion

The method checks for UTI conformance of the requested types, preferring an exact match to conformance.

## Parameters

- `types`: An array of strings representing UTIs, arranged in order of preference (most preferred as the 0th element in the array).

## See Also

- [var types: [NSPasteboard.PasteboardType]](nspasteboarditem/types.md)
  An array of uniform type identifier strings of the data types that the receiver supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/availabletype(from:))*