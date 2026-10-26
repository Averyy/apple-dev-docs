# timestamp

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The relative time at which the acceleration event occurred.

## Declaration

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

#### Discussion

This value indicates the time relative to the device CPU time base register. Compare acceleration event timestamps to determine the elapsed time between them. Do not use a timestamp to determine the exact time at which an event occurred.

## See Also

### Accessing the acceleration values
- [x](./x.md)
  The acceleration value for the x axis of the device.
- [y](./y.md)
  The acceleration value for the y axis of the device.
- [z](./z.md)
  The acceleration value for the z axis of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiacceleration/timestamp)*