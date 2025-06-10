# SCContentSharingPickerMode

**Framework**: ScreenCaptureKit  
**Kind**: struct

Available modes for selecting streaming content from a picker presented by the operating system.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
struct SCContentSharingPickerMode
```

## Topics

### Initializers
- [init(rawValue: UInt)](sccontentsharingpickermode/init(rawvalue:).md)
  Initializes a sharing-picker mode.
### Picker selection modes
- [static var multipleApplications: SCContentSharingPickerMode](sccontentsharingpickermode/multipleapplications.md)
  The mode allowing the selection of multiple applications through the presented picker.
- [static var multipleWindows: SCContentSharingPickerMode](sccontentsharingpickermode/multiplewindows.md)
  The mode allowing the selection of multiple windows through the presented picker.
- [static var singleApplication: SCContentSharingPickerMode](sccontentsharingpickermode/singleapplication.md)
  The mode allowing the selection of a single application through the presented picker.
- [static var singleDisplay: SCContentSharingPickerMode](sccontentsharingpickermode/singledisplay.md)
  The mode allowing the selection of a single display through the presented picker.
- [static var singleWindow: SCContentSharingPickerMode](sccontentsharingpickermode/singlewindow.md)
  The mode allowing the selection of a single window through the presented picker.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class SCContentSharingPicker](sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerConfiguration](sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [protocol SCContentSharingPickerObserver](sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickermode)*