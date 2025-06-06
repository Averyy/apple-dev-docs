# TVLockupViewComponent

**Framework**: TVUIKit  
**Kind**: protocol

The protocol for responding to lockup view state changes.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
protocol TVLockupViewComponent : NSObjectProtocol
```

## Topics

### Updating the Lockup View Appearance
- [func updateAppearance(forLockupViewState: UIControl.State)](tvlockupviewcomponent/updateappearance(forlockupviewstate:).md)
  Provides an opportunity to change the appearance of a view when a state changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [TVLockupHeaderFooterView](tvlockupheaderfooterview.md)

## See Also

- [class TVLockupView](tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [class TVLockupHeaderFooterView](tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVCardView](tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupviewcomponent)*