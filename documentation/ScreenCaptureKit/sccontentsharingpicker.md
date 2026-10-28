# SCContentSharingPicker

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

An instance of a picker presented by the operating system for managing frame-capture streams.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class SCContentSharingPicker
```

```objc
@interface SCContentSharingPicker : NSObject
```

## Overview

> ❗ **Important**:  Avoid creating your own sharing picker. Use the picker provided by the [`shared`](./sccontentsharingpicker/shared.md) static property.

## Topics

### Shared system picker
- [class var shared: SCContentSharingPicker](./sccontentsharingpicker/shared.md)
  The system-provided picker UI instance for capturing display and audio content from someone’s Mac.
### Picker availability
- [var isActive: Bool](./sccontentsharingpicker/isactive.md)
  A Boolean value that indicates if the picker is active.
### Stream configuration
- [func setConfiguration(SCContentSharingPickerConfiguration?, for: SCStream)](./sccontentsharingpicker/setconfiguration%28_,for%29.md)
  Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.
- [var configuration: SCContentSharingPickerConfiguration?](./sccontentsharingpicker/configuration.md)
  Sets the configuration for the content capture picker for all streams, providing allowed selection modes and content excluded from selection.
- [var defaultConfiguration: SCContentSharingPickerConfiguration](./sccontentsharingpicker/defaultconfiguration-94q2b.md)
  The default configuration to use for the content capture picker.
- [var maximumStreamCount: Int?](./sccontentsharingpicker/maximumstreamcount-2kuaa.md)
  The maximum number of streams the content capture picker allows.
- [- setConfiguration:forStream:](./sccontentsharingpicker/setconfiguration_forstream_.md)
  Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.
- [defaultConfiguration](./sccontentsharingpicker/defaultconfiguration-9v5sa.md)
  The default configuration to use for the content capture picker.
- [maximumStreamCount](./sccontentsharingpicker/maximumstreamcount-66khx.md)
  The maximum number of streams the content capture picker allows.
### Manage observers
- [func add(any SCContentSharingPickerObserver)](./sccontentsharingpicker/add%28_%29.md)
  Adds an observer instance to notify of changes in the content-sharing picker.
- [func remove(any SCContentSharingPickerObserver)](./sccontentsharingpicker/remove%28_%29.md)
  Removes an observer instance from the content-sharing picker.
### Picker display
- [func present()](./sccontentsharingpicker/present%28%29.md)
  Displays the picker with no active selection for capture.
- [func present(for: SCStream)](./sccontentsharingpicker/present%28for%29.md)
  Displays the picker with an already running capture stream.
- [func present(using: SCShareableContentStyle)](./sccontentsharingpicker/present%28using%29.md)
  Displays the picker for a single type of capture selection.
- [func present(for: SCStream, using: SCShareableContentStyle)](./sccontentsharingpicker/present%28for,using%29.md)
  Displays the picker with an existing capture stream, allowing for a single type of capture selection.
### Instance Properties
- [var isAvailable: Bool](./sccontentsharingpicker/isavailable.md)
### Instance Methods
- [func presentForCurrentApplication()](./sccontentsharingpicker/presentforcurrentapplication%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### System content-sharing picker
- [struct SCContentSharingPickerConfiguration](./sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [struct SCContentSharingPickerMode](./sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [protocol SCContentSharingPickerObserver](./sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.
- [SCContentSharingPickerConfiguration](./sccontentsharingpickerconfiguration-c.class.md)
  An instance for configuring the system content-sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker)*