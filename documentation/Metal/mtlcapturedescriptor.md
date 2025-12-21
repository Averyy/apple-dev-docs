# MTLCaptureDescriptor

**Framework**: Metal  
**Kind**: class

A configuration for a Metal capture session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MTLCaptureDescriptor
```

## Topics

### Setting capture parameters
- [var captureObject: Any?](mtlcapturedescriptor/captureobject.md)
  The instance whose contents should be captured.
- [var destination: MTLCaptureDestination](mtlcapturedescriptor/destination.md)
  The destination for any captured command data.
- [var outputURL: URL?](mtlcapturedescriptor/outputurl.md)
  A URL for a file to write the capture data into.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLCaptureManager](mtlcapturemanager.md)
  An instance you use to capture Metal command data in your app.
- [enum MTLCaptureDestination](mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](mtlcapturescope.md)
  A type that can programmatically customize a GPU frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor)*