# AVCaptureBracketedStillImageSettings

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

The abstract superclass for bracketed photo capture settings.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureBracketedStillImageSettings
```

```objc
@interface AVCaptureBracketedStillImageSettings : NSObject
```

#### Overview

> **Note**:  The `AVCaptureBracketedStillImageSettings` class must not be instantiated directly. You should create instances of the `AVCaptureManualExposureBracketedStillImageSettings` and `AVCaptureAutoExposureBracketedStillImageSettings` classes as appropriate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVCaptureAutoExposureBracketedStillImageSettings](./avcaptureautoexposurebracketedstillimagesettings.md)
- [AVCaptureManualExposureBracketedStillImageSettings](./avcapturemanualexposurebracketedstillimagesettings.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Bracketed settings types
- [class AVCaptureAutoExposureBracketedStillImageSettings](./avcaptureautoexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [class AVCaptureManualExposureBracketedStillImageSettings](./avcapturemanualexposurebracketedstillimagesettings.md)
  A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebracketedstillimagesettings)*