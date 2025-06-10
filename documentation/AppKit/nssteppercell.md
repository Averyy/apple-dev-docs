# NSStepperCell

**Framework**: AppKit  
**Kind**: class

An `NSStepperCell` object controls the appearance and behavior of an [`NSStepper`](nsstepper.md) object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSStepperCell
```

## Topics

### Specifying value range
- [var maxValue: Double](nssteppercell/maxvalue.md)
  The maximum value for the receiver.
- [var minValue: Double](nssteppercell/minvalue.md)
  The minimum value for the receiver.
- [var increment: Double](nssteppercell/increment.md)
  The amount by which the receiver will change per increment or decrement.
### Specifying how stepper cell responds
- [var autorepeat: Bool](nssteppercell/autorepeat.md)
  A Boolean value indicating how the receiver responds to mouse events.
- [var valueWraps: Bool](nssteppercell/valuewraps.md)
  A Boolean value indicating whether the receiver wraps around the minimum and maximum values.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppercell)*