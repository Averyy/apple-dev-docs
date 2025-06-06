# MERAWProcessorNotification

**Framework**: MediaExtension  
**Kind**: enum

Notifications that indicate a RAW processor state change.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum MERAWProcessorNotification
```

## Topics

### Type Properties
- [static let readyForMoreMediaDataDidChange: NSNotification.Name](merawprocessornotification/readyformoremediadatadidchange.md)
  A notification that indicates a change to the object’s readiness to process additional media data.
- [static let valuesDidChange: NSNotification.Name](merawprocessornotification/valuesdidchange.md)
  A notification that indicates a change to the object’s set of available processing parameters.

## See Also

- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessornotification)*