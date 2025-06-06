# AVCaptureIndexPicker

**Framework**: AVFoundation  
**Kind**: class

A control for selecting from a set of mutually exclusive values by index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
class AVCaptureIndexPicker
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Overview

Index pickers are appropriate for controls that provide an indexed container of values.

## Topics

### Creating an index picker
- [init(String, symbolName: String, numberOfIndexes: Int)](avcaptureindexpicker/init(_:symbolname:numberofindexes:).md)
  Creates a control to pick a value from the specified number of indexes.
- [init(String, symbolName: String, numberOfIndexes: Int, localizedTitleTransform: (Int) -> String)](avcaptureindexpicker/init(_:symbolname:numberofindexes:localizedtitletransform:).md)
  Creates a control to pick a value from the specified number of indices.
- [init(String, symbolName: String, localizedIndexTitles: [String])](avcaptureindexpicker/init(_:symbolname:localizedindextitles:).md)
  Creates an object to select an index from a set of values.
### Handling interaction
- [func setActionQueue(DispatchQueue, action: (Int) -> ())](avcaptureindexpicker/setactionqueue(_:action:).md)
  Sets the action to perform on the specified dispatch queue when the control’s value changes.
### Accessing the control value
- [var selectedIndex: Int](avcaptureindexpicker/selectedindex.md)
  The currently selected index.
- [var numberOfIndexes: Int](avcaptureindexpicker/numberofindexes.md)
  The number of index values the control provides.
### Setting an accessibility identifier
- [var accessibilityIdentifier: String?](avcaptureindexpicker/accessibilityidentifier.md)
  A string identifier for this control.
### Inspecting presentation attributes
- [var symbolName: String](avcaptureindexpicker/symbolname.md)
  The name of the SF Symbol that represents this control.
- [var localizedTitle: String](avcaptureindexpicker/localizedtitle.md)
  A localized title that describes the control’s action.
- [var localizedIndexTitles: [String]](avcaptureindexpicker/localizedindextitles.md)
  The titles to present for each index.

## Relationships

### Inherits From
- [AVCaptureControl](avcapturecontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)
  Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [class AVCaptureControl](avcapturecontrol.md)
  An abstract base class for controls that interact with the camera system.
- [class AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)
  A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [class AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md)
  A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [class AVCaptureSlider](avcaptureslider.md)
  A slider control that selects a value from a bounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker)*