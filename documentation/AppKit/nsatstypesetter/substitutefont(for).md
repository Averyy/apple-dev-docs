# substituteFont(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a screen font suitable for use in place of the specified original font,.

**Availability**:
- macOS

## Declaration

```swift
func substituteFont(for originalFont: NSFont) -> NSFont
```

```objc
- (NSFont *) substituteFontForFont:(NSFont *) originalFont;
```

## Discussion

A screen font can be substituted if the receiver is set to use screen fonts and if no [`NSTextView`](../nstextview.md) associated with the receiver is scaled or rotated. If a suitable screen font isn’t available or usable, this method returns the original font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/substitutefont(for:))*