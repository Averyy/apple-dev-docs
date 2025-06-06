# MERAWProcessorPixelBufferManager

**Framework**: MediaExtension  
**Kind**: class

Describes pixel buffer requirements and creates new pixel buffers.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class MERAWProcessorPixelBufferManager
```

#### Discussion

It contains the interfaces that the [`MERAWProcessor`](merawprocessor.md) uses for two tasks. First, to declare its set of requirements for output [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) in the form of a [`pixelBufferAttributes`](merawprocessorpixelbuffermanager/pixelbufferattributes-2cki6.md) dictionary. Second, create pixel buffers that match processor output requirements and satisfy Video Toolbox and client requirements.

## Topics

### Creating a pixel buffer
- [var pixelBufferAttributes: [String : any Sendable]](merawprocessorpixelbuffermanager/pixelbufferattributes-4fe69.md)
  A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the video RAW processor.
- [func makePixelBuffer() throws -> CVPixelBuffer](merawprocessorpixelbuffermanager/makepixelbuffer.md)
  Generates a pixel buffer using the session’s pixel buffer pool.

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

- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorpixelbuffermanager)*