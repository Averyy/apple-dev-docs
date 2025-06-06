# constraintsAffectingLayout(for:)

**Framework**: AppKit  
**Kind**: method

Returns the constraints impacting the layout of the view for a given orientation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func constraintsAffectingLayout(for orientation: NSLayoutConstraint.Orientation) -> [NSLayoutConstraint]
```

#### Return Value

The constraints impacting the layout of the view for the specified orientation.

#### Discussion

The returned set of constraints may not all include the view explicitly. Constraints that impact the location of the view implicitly may also be included. While this provides a good starting point for debugging, there is no guarantee that the returned set of constraints will include all of the constraints that have an impact on the view’s layout in the given orientation.

This method should only be used for debugging constraint-based layout. No application should ship with calls to this method as part of its operation.

## Parameters

- `orientation`: The direction of the dimension for which the constraints should be found.

## See Also

- [var hasAmbiguousLayout: Bool](nsview/hasambiguouslayout.md)
  A Boolean value indicating whether the constraints impacting the layout of the view incompletely specify the location of the view.
- [func exerciseAmbiguityInLayout()](nsview/exerciseambiguityinlayout.md)
  Randomly changes the frame of a view with an ambiguous layout between the different valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/constraintsaffectinglayout(for:))*