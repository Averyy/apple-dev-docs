# sizeToFit()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resizes the receiver to fit its text.

**Availability**:
- macOS

## Declaration

```swift
func sizeToFit()
```

```objc
- (void) sizeToFit;
```

#### Discussion

The text view will not be sized any smaller than its minimum size, however.

## See Also

### Constraining size
- [var maxSize: NSSize](./maxsize.md)
  The receiver’s maximum size.
- [var minSize: NSSize](./minsize.md)
  The receiver’s minimum size.
- [var isVerticallyResizable: Bool](./isverticallyresizable.md)
  A Boolean that controls whether the receiver changes its height to fit the height of its text.
- [var isHorizontallyResizable: Bool](./ishorizontallyresizable.md)
  A Boolean that controls whether the receiver changes its width to fit the width of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/sizetofit())*