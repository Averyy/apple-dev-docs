# unknown

**Framework**: Core Motion  
**Kind**: property

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

#### Discussion

This property is set to [`true`](https://developer.apple.com/documentation/Swift/true) when there is no way to estimate the current type of motion. For example, this property might be [`true`](https://developer.apple.com/documentation/Swift/true) if the device was turned on recently and not enough motion data had been gathered to determine the type of motion.

## See Also

- [var stationary: Bool](cmmotionactivity/stationary.md)
  A Boolean indicating whether the device is stationary.
- [var walking: Bool](cmmotionactivity/walking.md)
  A Boolean indicating whether the device is on a walking person.
- [var running: Bool](cmmotionactivity/running.md)
  A Boolean indicating whether the device is on a running person.
- [var automotive: Bool](cmmotionactivity/automotive.md)
  A Boolean indicating whether the device is in an automobile.
- [var cycling: Bool](cmmotionactivity/cycling.md)
  A Boolean indicating whether the device is in a bicycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivity/unknown)*