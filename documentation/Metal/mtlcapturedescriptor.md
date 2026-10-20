# MTLCaptureDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTLCaptureDescriptor : NSObject
```

## Topics

### Setting capture parameters
- [var captureObject: Any?](./mtlcapturedescriptor/captureobject.md)
  The instance whose contents should be captured.
- [var destination: MTLCaptureDestination](./mtlcapturedescriptor/destination.md)
  The destination for any captured command data.
- [var outputURL: URL?](./mtlcapturedescriptor/outputurl.md)
  A URL for a file to write the capture data into.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Frame capture
- [class MTLCaptureManager](./mtlcapturemanager.md)
  An instance you use to capture Metal command data in your app.
- [enum MTLCaptureDestination](./mtlcapturedestination.md)
  The kinds of destinations for captured command data.
- [protocol MTLCaptureScope](./mtlcapturescope.md)
  A type that can programmatically customize a GPU frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturedescriptor)*