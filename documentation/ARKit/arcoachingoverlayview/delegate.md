# delegate

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An object you supply that implements coaching event callbacks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@IBOutlet
weak var delegate: (any ARCoachingOverlayViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<ARCoachingOverlayViewDelegate> delegate;
```

## Discussion

Normally, you set the value of this property to your app’s view controller.

## See Also

### Delegating Events
- [protocol ARCoachingOverlayViewDelegate](../arcoachingoverlayviewdelegate.md)
  A set of callbacks you implement to be notified of coaching events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcoachingoverlayview/delegate)*