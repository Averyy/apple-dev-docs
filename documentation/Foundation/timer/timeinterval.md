# timeInterval

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The timer’s time interval, in seconds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeInterval: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval timeInterval;
```

#### Discussion

If the timer is non-repeating, returns `0` even if a time interval was set.

## See Also

### Retrieving Timer Information
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether the timer is currently valid.
- [var fireDate: Date](./firedate.md)
  The date at which the timer will fire.
- [var userInfo: Any?](./userinfo.md)
  The receiver’s `userInfo` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/timeinterval)*