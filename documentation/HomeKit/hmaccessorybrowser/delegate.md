# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A delegate that receives updates on the discovered accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any HMAccessoryBrowserDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<HMAccessoryBrowserDelegate> delegate;
```

## See Also

### Tracking the addition or removal of accessories
- [protocol HMAccessoryBrowserDelegate](../hmaccessorybrowserdelegate.md)
  An interface used to notify an accessory browser delegate of new accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/delegate)*