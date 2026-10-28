# requiresConstraintBasedLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value indicating whether the view depends on the constraint-based layout system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var requiresConstraintBasedLayout: Bool { get }
```

```objc
@property (class, readonly) BOOL requiresConstraintBasedLayout;
```

## Return Value

[`true`](../../Swift/true.md) if the view must be in a window using constraint-based layout to function properly, [`false`](../../Swift/false.md) otherwise.

## Discussion

Custom views should override this to return [`true`](../../Swift/true.md) if they can not layout correctly using autoresizing.

## See Also

### Opting In to Auto Layout
- [var translatesAutoresizingMaskIntoConstraints: Bool](./translatesautoresizingmaskintoconstraints.md)
  A Boolean value indicating whether the view’s autoresizing mask is translated into constraints for the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/requiresconstraintbasedlayout)*