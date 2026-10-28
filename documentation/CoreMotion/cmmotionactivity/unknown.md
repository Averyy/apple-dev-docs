# unknown

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the type of motion is unknown.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 15.0+
- watchOS 2.0+

## Declaration

```swift
var unknown: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL unknown;
```

## Discussion

This property is set to [`true`](../../Swift/true.md) when there is no way to estimate the current type of motion. For example, this property might be [`true`](../../Swift/true.md) if the device was turned on recently and not enough motion data had been gathered to determine the type of motion.

## See Also

### Getting the Type of Motion
- [var stationary: Bool](./stationary.md)
  A Boolean indicating whether the device is stationary.
- [var walking: Bool](./walking.md)
  A Boolean indicating whether the device is on a walking person.
- [var running: Bool](./running.md)
  A Boolean indicating whether the device is on a running person.
- [var automotive: Bool](./automotive.md)
  A Boolean indicating whether the device is in an automobile.
- [var cycling: Bool](./cycling.md)
  A Boolean indicating whether the device is in a bicycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown)*