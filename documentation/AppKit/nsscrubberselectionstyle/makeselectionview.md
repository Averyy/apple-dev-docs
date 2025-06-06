# makeSelectionView()

**Framework**: AppKit  
**Kind**: method

Provides an opportunity to create a customized scrubber selection style.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func makeSelectionView() -> NSScrubberSelectionView?
```

#### Return Value

A correctly configured scrubber selection view that represents the appearance of your custom selection style.

#### Discussion

In an [`NSScrubberSelectionStyle`](nsscrubberselectionstyle.md) subclass that you create, override this method to create a custom selection style.

## See Also

- [init()](nsscrubberselectionstyle/init.md)
  Initializes a new scrubber selection style.
- [init(coder: NSCoder)](nsscrubberselectionstyle/init(coder:).md)
  Initializes a scrubber selection style when included from a nib or Storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionstyle/makeselectionview())*