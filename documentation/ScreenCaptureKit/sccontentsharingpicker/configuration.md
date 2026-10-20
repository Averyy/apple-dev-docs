# configuration

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

Sets the configuration for the content capture picker for all streams, providing allowed selection modes and content excluded from selection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var configuration: SCContentSharingPickerConfiguration? { get set }
```

## See Also

### Stream configuration
- [func setConfiguration(SCContentSharingPickerConfiguration?, for: SCStream)](./setconfiguration%28_,for%29.md)
  Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.
- [var defaultConfiguration: SCContentSharingPickerConfiguration](./defaultconfiguration-94q2b.md)
  The default configuration to use for the content capture picker.
- [var maximumStreamCount: Int?](./maximumstreamcount-2kuaa.md)
  The maximum number of streams the content capture picker allows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/configuration)*