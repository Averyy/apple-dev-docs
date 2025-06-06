# substituteFont(for:)

**Framework**: AppKit  
**Kind**: method

Returns a screen font suitable for use in place of a given font.

**Availability**:
- macOS ?+

## Declaration

```swift
func substituteFont(for originalFont: NSFont) -> NSFont
```

#### Return Value

A screen font suitable for use in place of `originalFont`. This method returns `originalFont` if a screen font can’t be used or isn’t available.

#### Discussion

A screen font can only be substituted if the receiver is set to use screen fonts and if no text view associated with the receiver is scaled or rotated.

## Parameters

- `originalFont`: The original font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/substitutefont(for:))*