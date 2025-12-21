# AVCaptionConversionValidator

**Framework**: AVFoundation  
**Kind**: class

An object that validates captions for a conversion operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionConversionValidator
```

## Topics

### Creating a validator
- [init(captions: [AVCaption], timeRange: CMTimeRange, conversionSettings: [AVCaptionSettingsKey : Any])](avcaptionconversionvalidator/init(captions:timerange:conversionsettings:).md)
  Creates an object that validates captions for a conversion operation.
### Inspecting the validator
- [var captions: [AVCaption]](avcaptionconversionvalidator/captions.md)
  The array of captions that the system validates.
- [var timeRange: CMTimeRange](avcaptionconversionvalidator/timerange.md)
  The time range of the media timeline in which the captions must exist.
### Validating captions
- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](avcaptionconversionvalidator/validatecaptionconversion(warninghandler:).md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](avcaptionconversionvalidator/warnings.md)
  The collection of warnings the validator encountered.
- [class AVCaptionConversionWarning](avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.
- [func stopValidating()](avcaptionconversionvalidator/stopvalidating.md)
  Stops the active validation operation.
### Checking the status
- [var status: AVCaptionConversionValidator.Status](avcaptionconversionvalidator/status-swift.property.md)
  A value that indicates the status of validation.
- [AVCaptionConversionValidator.Status](avcaptionconversionvalidator/status-swift.enum.md)
  Constants that indicate the status of a validator.

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

- [struct AVCaptionSettingsKey](avcaptionsettingskey.md)
  A structure that defines dictionary keys to configure the caption converter and validator.
- [class AVCaptionFormatConformer](avcaptionformatconformer.md)
  An object that converts a canonical caption to a specific format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator)*