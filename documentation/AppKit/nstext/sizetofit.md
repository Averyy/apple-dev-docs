# sizeToFit()

**Framework**: AppKit  
**Kind**: method

Resizes the receiver to fit its text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sizeToFit()
```

#### Discussion

The text view will not be sized any smaller than its minimum size, however.

## See Also

- [var maxSize: NSSize](nstext/maxsize.md)
  The receiver’s maximum size.
- [var minSize: NSSize](nstext/minsize.md)
  The receiver’s minimum size.
- [var isVerticallyResizable: Bool](nstext/isverticallyresizable.md)
  A Boolean that controls whether the receiver changes its height to fit the height of its text.
- [var isHorizontallyResizable: Bool](nstext/ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/sizetofit())*