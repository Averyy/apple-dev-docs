# translatesAutoresizingMaskIntoConstraints

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view’s autoresizing mask is translated into constraints for the constraint-based layout system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var translatesAutoresizingMaskIntoConstraints: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the view’s superview looks at the view’s autoresizing mask, produces constraints that implement it, and adds those constraints to itself (the superview). If your view has flexible constraints that require dynamic adjustment, set this property to [`false`](https://developer.apple.com/documentation/swift/false) and apply the constraints yourself.

## See Also

- [class var requiresConstraintBasedLayout: Bool](nsview/requiresconstraintbasedlayout.md)
  Returns a Boolean value indicating whether the view depends on the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translatesautoresizingmaskintoconstraints)*