# automotive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the device is in an automobile.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 15.0+
- watchOS 2.0+

## Declaration

```swift
var automotive: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL automotive;
```

## See Also

### Getting the Type of Motion
- [var stationary: Bool](./stationary.md)
  A Boolean indicating whether the device is stationary.
- [var walking: Bool](./walking.md)
  A Boolean indicating whether the device is on a walking person.
- [var running: Bool](./running.md)
  A Boolean indicating whether the device is on a running person.
- [var cycling: Bool](./cycling.md)
  A Boolean indicating whether the device is in a bicycle.
- [var unknown: Bool](./unknown.md)
  A Boolean indicating whether the type of motion is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivity/automotive)*