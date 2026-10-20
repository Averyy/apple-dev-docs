# visibilityPriority(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the visibility priority for a specified view in the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func visibilityPriority(for view: NSView) -> NSStackView.VisibilityPriority
```

```objc
- (NSStackViewVisibilityPriority) visibilityPriorityForView:(NSView *) view;
```

#### Return Value

The visibility priority for the specified view.

#### Discussion

Visibility priority is the Auto Layout priority for a view to remain attached to a stack view when Auto Layout reduces the stack view’s size (such as when a user reduces the enclosing window’s size).

## Parameters

- `view`: The view that you are getting the visibility priority for.

## See Also

### Configuring Views in a Stack View
- [func customSpacing(after: NSView) -> CGFloat](./customspacing%28after%29.md)
  Returns the custom spacing, in points, between a specified view in the stack view and the view that follows it.
- [func setCustomSpacing(CGFloat, after: NSView)](./setcustomspacing%28_,after%29.md)
  Specifies the custom spacing, in points, between a specified view and the view that follows it in the stack view.
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](./setvisibilitypriority%28_,for%29.md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [NSStackView.VisibilityPriority](./visibilitypriority.md)
  The various Auto Layout priorities for a view in the stack view to remain attached.
- [class let useDefaultSpacing: CGFloat](./usedefaultspacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/visibilitypriority(for:))*