# activeToolPicker

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The current tool picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var activeToolPicker: PKToolPicker? { get set }
```

```objc
@property (nonatomic, strong, nullable) PKToolPicker * activeToolPicker;
```

#### Discussion

Control tool picker visibility with the `toolPickerVisibility` property.

If `nil` the active tool picker is based on the next responder.

## See Also

### Configuring the tool picker
- [enum PKToolPickerVisibility](../pktoolpickervisibility.md)
  Constants that describe the visibility state of a tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkresponderstate/activetoolpicker)*