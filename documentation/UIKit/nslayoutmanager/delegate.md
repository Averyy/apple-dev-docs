# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout manager’s delegate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any NSLayoutManagerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<NSLayoutManagerDelegate> delegate;
```

## See Also

### Managing the layout process
- [protocol NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)
  A set of optional methods that delegates of layout manager objects implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/delegate)*