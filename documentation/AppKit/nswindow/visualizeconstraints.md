# visualizeConstraints(_:)

**Framework**: AppKit  
**Kind**: method

Displays a visual representation of the supplied constraints in the window.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func visualizeConstraints(_ constraints: [NSLayoutConstraint]?)
```

#### Discussion

The constraints to visualize are typically discovered by identifying a view whose layout is unexpected and then calling [`constraintsAffectingLayout(for:)`](nsview/constraintsaffectinglayout(for:).md) on that view.

This method should only be used for debugging constraint-based layout. No application should ship with calls to this method as part of its operation.

## Parameters

- `constraints`: The constraints to visualize. All constraints must be held by views in the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/visualizeconstraints(_:))*