# MERAWProcessorExtension

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines a factory to create RAW processors for a codec type that the extension implements.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol MERAWProcessorExtension : NSObjectProtocol
```

#### Discussion

This protocol provides a factory method to create a new [`MERAWProcessor`](merawprocessor.md) instance for a codecType implemented by the extension. The Video Toolbox instantiates a single [`MERAWProcessorExtension`](merawprocessorextension.md), and creates individual [`MERAWProcessor`](merawprocessor.md) instances as needed. If the `CMVideoFormatDescription` passed to [`makeProcessor(formatDescription:pixelBufferManager:)`](merawprocessorextension/makeprocessor(formatdescription:pixelbuffermanager:).md) is not compatible with the [`MERAWProcessor`](merawprocessor.md) implementation, the factory call should fail and return [`MEError.Code.unsupportedFeature`](meerror-swift.struct/code/unsupportedfeature.md).

## Topics

### Creating an extension
- [init()](merawprocessorextension/init.md)
  Creates a video RAW processor factory.
### Creating a RAW processor
- [func makeProcessor(formatDescription: CMVideoFormatDescription, pixelBufferManager: MERAWProcessorPixelBufferManager) throws -> any MERAWProcessor](merawprocessorextension/makeprocessor(formatdescription:pixelbuffermanager:).md)
  A factory method to create a video RAW processor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorextension)*