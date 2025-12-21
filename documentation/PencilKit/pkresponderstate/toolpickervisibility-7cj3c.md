# toolPickerVisibility

**Framework**: PencilKit  
**Kind**: property

The visibility state of the tool picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var toolPickerVisibility: PKToolPickerVisibility? { get set }
```

#### Discussion

This controls the state of the tool picker that is provided by the `activeToolPicker` property.

If `nil` tool picker visibility is based on the next responder. If no responder provides a visibility, the default is `.visible`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkresponderstate/toolpickervisibility-7cj3c)*