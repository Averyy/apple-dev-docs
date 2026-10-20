# AVCaptionConversionValidator

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionConversionValidator : NSObject
```

## Topics

### Creating a validator
- [init(captions: [AVCaption], timeRange: CMTimeRange, conversionSettings: [AVCaptionSettingsKey : Any])](./avcaptionconversionvalidator/init%28captions,timerange,conversionsettings%29.md)
  Creates an object that validates captions for a conversion operation.
### Inspecting the validator
- [var captions: [AVCaption]](./avcaptionconversionvalidator/captions.md)
  The array of captions that the system validates.
- [var timeRange: CMTimeRange](./avcaptionconversionvalidator/timerange.md)
  The time range of the media timeline in which the captions must exist.
### Validating captions
- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](./avcaptionconversionvalidator/validatecaptionconversion%28warninghandler%29.md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](./avcaptionconversionvalidator/warnings.md)
  The collection of warnings the validator encountered.
- [class AVCaptionConversionWarning](./avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.
- [func stopValidating()](./avcaptionconversionvalidator/stopvalidating%28%29.md)
  Stops the active validation operation.
### Checking the status
- [var status: AVCaptionConversionValidator.Status](./avcaptionconversionvalidator/status-swift.property.md)
  A value that indicates the status of validation.
- [AVCaptionConversionValidator.Status](./avcaptionconversionvalidator/status-swift.enum.md)
  Constants that indicate the status of a validator.

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

### Conversion and validation
- [struct AVCaptionSettingsKey](./avcaptionsettingskey.md)
  A structure that defines dictionary keys to configure the caption converter and validator.
- [class AVCaptionFormatConformer](./avcaptionformatconformer.md)
  An object that converts a canonical caption to a specific format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator)*