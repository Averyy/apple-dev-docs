# maximumStreamCount

**Framework**: ScreenCaptureKit  
**Kind**: property

The maximum number of streams the content capture picker allows.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var maximumStreamCount: Int? { get set }
```

#### Discussion

The default value is `1`.

## See Also

- [func setConfiguration(SCContentSharingPickerConfiguration?, for: SCStream)](sccontentsharingpicker/setconfiguration(_:for:).md)
  Sets the configuration for the content capture picker for a capture stream, providing allowed selection modes and content excluded from selection.
- [var configuration: SCContentSharingPickerConfiguration?](sccontentsharingpicker/configuration.md)
  Sets the configuration for the content capture picker for all streams, providing allowed selection modes and content excluded from selection.
- [var defaultConfiguration: SCContentSharingPickerConfiguration](sccontentsharingpicker/defaultconfiguration-94q2b.md)
  The default configuration to use for the content capture picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker/maximumstreamcount-2kuaa)*