# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tab view’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSTabViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTabViewDelegate> delegate;
```

#### Discussion

The value of this property must conform to the [`NSTabViewDelegate`](../nstabviewdelegate.md) protocol.

## See Also

### Handling the Selection of Tabs
- [protocol NSTabViewDelegate](../nstabviewdelegate.md)
  The `NSTabViewDelegate` protocol defines the optional methods implemented by delegates of `NSTabView` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/delegate)*