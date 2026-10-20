# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The split view’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSSplitViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSSplitViewDelegate> delegate;
```

## See Also

### Customizing the Split View Behavior
- [protocol NSSplitViewDelegate](../nssplitviewdelegate.md)
  A set of optional methods that a delegate of a split view implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/delegate)*