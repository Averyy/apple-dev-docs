# removeView(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a specified view from the stack view.

**Availability**:
- macOS

## Declaration

```swift
func removeView(_ view: NSView)
```

```objc
- (void) removeView:(NSView *) view;
```

## Discussion

This method removes a view from a stack view whether the view is attached or detached. For an attached view only, you can alternatively call the [`removeFromSuperview()`](../../UIKit/uiview/removefromsuperview%28%29.md) method on the view.

## Parameters

- `view`: The view you want to remove from the stack view.

  > ❗ **Important**:  If you attempt to remove a view that is not in the stack view, the system raises an exception.

## See Also

### Managing Views in Gravity Areas
- [func addView(NSView, in: NSStackView.Gravity)](./addview%28_,in%29.md)
  Adds a view to the end of the stack view gravity area.
- [func insertView(NSView, at: Int, in: NSStackView.Gravity)](./insertview%28_,at,in%29.md)
  Adds a view to a stack view gravity area at a specified index position.
- [func setViews([NSView], in: NSStackView.Gravity)](./setviews%28_,in%29.md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [NSStackView.Gravity](./gravity.md)
  The gravity areas available in a stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/removeview(_:))*