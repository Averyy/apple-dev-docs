# allowsRotation

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the profile reports the directional pad values relative to its current orientation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsRotation: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsRotation;
```

#### Discussion

If this property is [`false`](../../Swift/false.md), the profile reports the value of the directional pad only in portrait orientation even when the user rotates the controller. If this property is [`true`](../../Swift/true.md), the profile reports the values using the current orientation. The default value for this property is [`false`](../../Swift/false.md).

## See Also

### Getting directional pad inputs
- [var dpad: GCControllerDirectionPad](./dpad.md)
  The controller’s directional pad element.
- [var reportsAbsoluteDpadValues: Bool](./reportsabsolutedpadvalues.md)
  A Boolean value that indicates whether the directional pad reports absolute or relative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/allowsrotation)*