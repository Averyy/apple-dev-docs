# hasAmbiguousLayout

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the constraints impacting the layout of the view incompletely specify the location of the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var hasAmbiguousLayout: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the view’s location or size cannot be determined definitively based on the current constraints.

Accessing this property engages the layout engine to determine whether any other frame would also satisfy the constraints on the view. Because this process involves laying out the view, accessing the property can be an expensive operation but it can also provide useful debugging information. AppKit automatically calls this method when a window is asked to visualize its constraints using the [`visualizeConstraints(_:)`](nswindow/visualizeconstraints(_:).md) method.

> ❗ **Important**:  This property should be used only for debugging constraint-based layout. Do not access this property in the shipping version of your app.

 This property should be used only for debugging constraint-based layout. Do not access this property in the shipping version of your app.

## See Also

- [func constraintsAffectingLayout(for: NSLayoutConstraint.Orientation) -> [NSLayoutConstraint]](nsview/constraintsaffectinglayout(for:).md)
  Returns the constraints impacting the layout of the view for a given orientation.
- [func exerciseAmbiguityInLayout()](nsview/exerciseambiguityinlayout.md)
  Randomly changes the frame of a view with an ambiguous layout between the different valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/hasambiguouslayout)*