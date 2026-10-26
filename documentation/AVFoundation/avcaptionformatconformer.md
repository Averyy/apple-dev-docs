# AVCaptionFormatConformer

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that converts a canonical caption to a specific format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionFormatConformer
```

```objc
@interface AVCaptionFormatConformer : NSObject
```

## Topics

### Creating a format conformer
- [init(conversionSettings: [AVCaptionSettingsKey : Any])](./avcaptionformatconformer/init%28conversionsettings%29.md)
  Creates a new object with format conversion settings.
- [+ captionFormatConformerWithConversionSettings:](./avcaptionformatconformer/captionformatconformerwithconversionsettings_.md)
  A class method that creates a new object with format conversion settings.
### Conforming captions
- [var conformsCaptionsToTimeRange: Bool](./avcaptionformatconformer/conformscaptionstotimerange.md)
  A Boolean value that indicates whether to conform the time range of a canonical caption.
- [func conformedCaption(for: AVCaption) throws -> AVCaption](./avcaptionformatconformer/conformedcaption%28for%29.md)
  Creates a caption that conforms to a specific format.

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
- [class AVCaptionConversionValidator](./avcaptionconversionvalidator.md)
  An object that validates captions for a conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer)*