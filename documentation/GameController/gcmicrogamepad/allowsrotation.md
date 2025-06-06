# allowsRotation

**Framework**: Game Controller  
**Kind**: property

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

#### Discussion

If this property is [`false`](https://developer.apple.com/documentation/swift/false), the profile reports the value of the directional pad only in portrait orientation even when the user rotates the controller. If this property is [`true`](https://developer.apple.com/documentation/swift/true), the profile reports the values using the current orientation. The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var dpad: GCControllerDirectionPad](gcmicrogamepad/dpad.md)
  The controller’s directional pad element.
- [var reportsAbsoluteDpadValues: Bool](gcmicrogamepad/reportsabsolutedpadvalues.md)
  A Boolean value that indicates whether the directional pad reports absolute or relative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/allowsrotation)*