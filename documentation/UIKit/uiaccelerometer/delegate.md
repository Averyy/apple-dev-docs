# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate object you want to receive acceleration events.

## Declaration

```objc
@property (nonatomic, weak, nullable) id<UIAccelerometerDelegate> delegate;
```

## Discussion

The [`UIAccelerometerDelegate`](../uiaccelerometerdelegate.md) is a formal protocol, so your delegate object must implement the method it defines. The shared accelerometer object delivers the acceleration data to your delegate at the specified interval. It delivers these events on the main thread of your application when it is in the NSDefaultRunLoopMode run loop mode.

## See Also

### Accessing the accelerometer properties
- [updateInterval](./updateinterval.md)
  The interval at which to deliver acceleration data to the delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccelerometer/delegate)*