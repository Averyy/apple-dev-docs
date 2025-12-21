# PKResponderState

**Framework**: PencilKit  
**Kind**: class

The state of PencilKit behavior related to a `UIResponder`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
class PKResponderState
```

#### Overview

Control the behavior of responders via the `UIResponder.pencilKitResponderState` property.

```swift
view.pencilKitResponderState.activeToolPicker = PKToolPicker()
view.pencilKitResponderState.toolPickerVisibility = .visible
```

## Topics

### Instance Properties
- [var activeToolPicker: PKToolPicker?](pkresponderstate/activetoolpicker.md)
  The current tool picker.
- [var toolPickerVisibility: PKToolPickerVisibility?](pkresponderstate/toolpickervisibility-7cj3c.md)
  The visibility state of the tool picker.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkresponderstate)*