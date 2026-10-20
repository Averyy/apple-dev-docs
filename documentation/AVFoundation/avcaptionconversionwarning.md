# AVCaptionConversionWarning

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that represents a conversion warning produced by a validator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionConversionWarning
```

```objc
@interface AVCaptionConversionWarning : NSObject
```

## Topics

### Inspecting the warning
- [var warningType: AVCaptionConversionWarning.WarningType](./avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](./avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](./avcaptionconversionwarning/adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [class AVCaptionConversionAdjustment](./avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [AVCaptionConversionWarning.WarningType](./avcaptionconversionwarning/warningtype-swift.struct.md)
  The type of a caption conversion warning.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Validating captions
- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](./avcaptionconversionvalidator/validatecaptionconversion%28warninghandler%29.md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](./avcaptionconversionvalidator/warnings.md)
  The collection of warnings the validator encountered.
- [func stopValidating()](./avcaptionconversionvalidator/stopvalidating%28%29.md)
  Stops the active validation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning)*