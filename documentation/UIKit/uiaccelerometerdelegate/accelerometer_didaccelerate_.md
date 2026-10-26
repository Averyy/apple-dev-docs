# accelerometer:didAccelerate:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Delivers the latest acceleration data to the delegate.

## Declaration

```objc
- (void) accelerometer:(UIAccelerometer *) accelerometer didAccelerate:(UIAcceleration *) acceleration;
```

#### Discussion

The shared [`UIAccelerometer`](../uiaccelerometer.md) object invokes this method at the desired interval, providing your delegate with updated acceleration data each time.

This method is always invoked on your application’s main thread when it is in the NSDefaultRunLoopMode run loop mode.

## Parameters

- `accelerometer`: The application-wide accelerometer object.
- `acceleration`: The most recent acceleration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccelerometerdelegate/accelerometer:didaccelerate:)*