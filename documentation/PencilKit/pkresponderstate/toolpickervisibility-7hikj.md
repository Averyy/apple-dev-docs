# toolPickerVisibility

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The visibility state of the tool picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, assign) PKToolPickerVisibility toolPickerVisibility;
```

#### Discussion

This controls the state of the tool picker that is provided by the `activeToolPicker` property.

If `PKToolPickerVisibilityInherited` tool picker visibility is based on the next responder. If no responder provides a visibility, the default is `PKToolPickerVisibilityVisible`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkresponderstate/toolpickervisibility-7hikj)*