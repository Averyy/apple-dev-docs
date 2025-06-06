# setConfiguration(_:for:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
func setConfiguration(_ configuration: SCContentSharingPickerConfiguration?, for stream: SCStream)
```

## Parameters

- `configuration`: The configuration to set for the given capture stream. When this value is  , changes the stream configuration to use  .
- `stream`: The capture stream to set a configuration for. When this value is  , applies to all currently active streams.

## See Also

- [var configuration: SCContentSharingPickerConfiguration?](sccontentsharingpicker/configuration.md)
  Sets the configuration for the content capture picker for all streams, providing allowed selection modes and content excluded from selection.
- [var defaultConfiguration: SCContentSharingPickerConfiguration](sccontentsharingpicker/defaultconfiguration-94q2b.md)
  The default configuration to use for the content capture picker.
- [var maximumStreamCount: Int?](sccontentsharingpicker/maximumstreamcount-2kuaa.md)
  The maximum number of streams the content capture picker allows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/setconfiguration(_:for:))*