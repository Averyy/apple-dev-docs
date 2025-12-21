# AVCaptionFormatConformer

**Framework**: AVFoundation  
**Kind**: class

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

## Topics

### Creating a format conformer
- [init(conversionSettings: [AVCaptionSettingsKey : Any])](avcaptionformatconformer/init(conversionsettings:).md)
  Creates a new object with format conversion settings.
### Conforming captions
- [var conformsCaptionsToTimeRange: Bool](avcaptionformatconformer/conformscaptionstotimerange.md)
  A Boolean value that indicates whether to conform the time range of a canonical caption.
- [func conformedCaption(for: AVCaption) throws -> AVCaption](avcaptionformatconformer/conformedcaption(for:).md)
  Creates a caption that conforms to a specific format.

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
- [class AVCaptionConversionValidator](avcaptionconversionvalidator.md)
  An object that validates captions for a conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer)*