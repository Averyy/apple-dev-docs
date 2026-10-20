# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The layout manager’s delegate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
weak var delegate: (any NSLayoutManagerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSLayoutManagerDelegate> delegate;
```

## See Also

### Managing the layout process
- [protocol NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)
  A set of optional methods that delegates of layout manager objects implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/delegate)*