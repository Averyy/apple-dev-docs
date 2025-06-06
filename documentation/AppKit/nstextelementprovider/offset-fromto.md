# offset(from:to:)

**Framework**: AppKit  
**Kind**: method

Returns the offset between the two specified locations.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

#### Return Value

An `Integer` that represents the offset between the starting and ending locations.

#### Discussion

The return value could be positive or negative. This method can return [`NSNotFound`](https://developer.apple.com/documentation/foundation/nsnotfound) when the method can’t represent an offset as an integer value. This can occur, for example, if the locations aren’t in the same document).

## Parameters

- `from`: A starting location.
- `to`: An ending location.

## See Also

- [func adjustedRange(from: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?](nstextelementprovider/adjustedrange(from:foreditingtextselection:).md)
  A method you implement if the location backing store requires manual adjustment after editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/offset(from:to:))*