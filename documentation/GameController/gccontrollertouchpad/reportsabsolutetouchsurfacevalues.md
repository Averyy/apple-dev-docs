# reportsAbsoluteTouchSurfaceValues

**Framework**: Game Controller  
**Kind**: property

A Boolean value that determines whether the touch values are absolute or relative.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var reportsAbsoluteTouchSurfaceValues: Bool { get set }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), the touch values are absolute on the surface of the touchpad. If this property is [`false`](https://developer.apple.com/documentation/swift/false), the touch values are relative to the first touch on a virtual directional pad. The default value for this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var touchState: GCControllerTouchpad.TouchState](gccontrollertouchpad/touchstate-swift.property.md)
  The state of the user’s touch on the surface of the touchpad.
- [GCControllerTouchpad.TouchState](gccontrollertouchpad/touchstate-swift.enum.md)
  The possible states of the user’s touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/reportsabsolutetouchsurfacevalues)*