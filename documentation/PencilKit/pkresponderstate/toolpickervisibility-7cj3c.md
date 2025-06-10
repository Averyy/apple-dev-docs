# toolPickerVisibility

**Framework**: PencilKit  
**Kind**: property

The visibility state of the tool picker.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var toolPickerVisibility: PKToolPickerVisibility? { get set }
```

#### Discussion

This controls the state of the tool picker that is provided by the `activeToolPicker` property.

If `nil` tool picker visibility is based on the next responder. If no responder provides a visibility, the default is `.visible`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkresponderstate/toolpickervisibility-7cj3c)*