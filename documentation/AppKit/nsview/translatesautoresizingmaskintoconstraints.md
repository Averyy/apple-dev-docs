# translatesAutoresizingMaskIntoConstraints

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view’s autoresizing mask is translated into constraints for the constraint-based layout system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var translatesAutoresizingMaskIntoConstraints: Bool { get set }
```

```objc
@property BOOL translatesAutoresizingMaskIntoConstraints;
```

#### Discussion

When this property is set to [`true`](../../Swift/true.md), the view’s superview looks at the view’s autoresizing mask, produces constraints that implement it, and adds those constraints to itself (the superview). If your view has flexible constraints that require dynamic adjustment, set this property to [`false`](../../Swift/false.md) and apply the constraints yourself.

## See Also

### Opting In to Auto Layout
- [class var requiresConstraintBasedLayout: Bool](./requiresconstraintbasedlayout.md)
  Returns a Boolean value indicating whether the view depends on the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translatesautoresizingmaskintoconstraints)*