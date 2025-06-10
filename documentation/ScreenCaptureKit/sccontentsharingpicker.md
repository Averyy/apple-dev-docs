# SCContentSharingPicker

**Framework**: ScreenCaptureKit  
**Kind**: class

An instance of a picker presented by the operating system for managing frame-capture streams.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
class SCContentSharingPicker
```

#### Overview

> ❗ **Important**:  Avoid creating your own sharing picker. Use the picker provided by the [`shared`](sccontentsharingpicker/shared.md) static property.

## Topics

### Shared system picker
- [class var shared: SCContentSharingPicker](sccontentsharingpicker/shared.md)
  The system-provided picker UI instance for capturing display and audio content from someone’s Mac.
### Picker availability
- [var isActive: Bool](sccontentsharingpicker/isactive.md)
  A Boolean value that indicates if the picker is active.
### Stream configuration
- [func setConfiguration(SCContentSharingPickerConfiguration?, for: SCStream)](sccontentsharingpicker/setconfiguration(_:for:).md)
  Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.
- [var configuration: SCContentSharingPickerConfiguration?](sccontentsharingpicker/configuration.md)
  Sets the configuration for the content capture picker for all streams, providing allowed selection modes and content excluded from selection.
- [var defaultConfiguration: SCContentSharingPickerConfiguration](sccontentsharingpicker/defaultconfiguration-94q2b.md)
  The default configuration to use for the content capture picker.
- [var maximumStreamCount: Int?](sccontentsharingpicker/maximumstreamcount-2kuaa.md)
  The maximum number of streams the content capture picker allows.
### Manage observers
- [func add(any SCContentSharingPickerObserver)](sccontentsharingpicker/add(_:).md)
  Adds an observer instance to notify of changes in the content-sharing picker.
- [func remove(any SCContentSharingPickerObserver)](sccontentsharingpicker/remove(_:).md)
  Removes an observer instance from the content-sharing picker.
### Picker display
- [func present()](sccontentsharingpicker/present.md)
  Displays the picker with no active selection for capture.
- [func present(for: SCStream)](sccontentsharingpicker/present(for:).md)
  Displays the picker with an already running capture stream.
- [func present(using: SCShareableContentStyle)](sccontentsharingpicker/present(using:).md)
  Displays the picker for a single type of capture selection.
- [func present(for: SCStream, using: SCShareableContentStyle)](sccontentsharingpicker/present(for:using:).md)
  Displays the picker with an existing capture stream, allowing for a single type of capture selection.

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

## See Also

- [struct SCContentSharingPickerConfiguration](sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [struct SCContentSharingPickerMode](sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [protocol SCContentSharingPickerObserver](sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker)*