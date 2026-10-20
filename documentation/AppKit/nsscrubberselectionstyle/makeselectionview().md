# makeSelectionView()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to create a customized scrubber selection style.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func makeSelectionView() -> NSScrubberSelectionView?
```

```objc
- (NSScrubberSelectionView *) makeSelectionView;
```

#### Return Value

A correctly configured scrubber selection view that represents the appearance of your custom selection style.

#### Discussion

In an [`NSScrubberSelectionStyle`](../nsscrubberselectionstyle.md) subclass that you create, override this method to create a custom selection style.

## See Also

### Creating a selection style
- [init()](./init%28%29.md)
  Initializes a new scrubber selection style.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Initializes a scrubber selection style when included from a nib or Storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionstyle/makeselectionview())*