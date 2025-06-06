# requiresConstraintBasedLayout

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value indicating whether the view depends on the constraint-based layout system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class var requiresConstraintBasedLayout: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view must be in a window using constraint-based layout to function properly, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Custom views should override this to return [`true`](https://developer.apple.com/documentation/swift/true) if they can not layout correctly using autoresizing.

## See Also

- [var translatesAutoresizingMaskIntoConstraints: Bool](nsview/translatesautoresizingmaskintoconstraints.md)
  A Boolean value indicating whether the view’s autoresizing mask is translated into constraints for the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/requiresconstraintbasedlayout)*