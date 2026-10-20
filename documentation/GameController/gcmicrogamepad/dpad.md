# dpad

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The controller’s directional pad element.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dpad: GCControllerDirectionPad { get }
```

```objc
@property (nonatomic, strong, readonly) GCControllerDirectionPad * dpad;
```

#### Discussion

The directional pad in the micro gamepad profile reports analog directional information.

## See Also

### Getting directional pad inputs
- [var reportsAbsoluteDpadValues: Bool](./reportsabsolutedpadvalues.md)
  A Boolean value that indicates whether the directional pad reports absolute or relative values.
- [var allowsRotation: Bool](./allowsrotation.md)
  A Boolean value that indicates whether the profile reports the directional pad values relative to its current orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/dpad)*