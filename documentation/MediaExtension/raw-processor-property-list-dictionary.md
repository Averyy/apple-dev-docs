# RAW processor property list dictionary

**Framework**: MediaExtension

Include a property list dictionary to describe a RAW processor.

#### Overview

A MediaExtension RAW processor needs to include an `EXAppExtensionAttributes` dictionary in its `Info.plist` file that contains the following keys and values:

- [`kMERAWProcessorClassImplementationIDKey`](kmerawprocessorclassimplementationidkey.md): A string that uniquely identifies the RAW processor. Start this string with your reverse domain identifier, and for clarity, include `.rawprocessor.` and the name of the codec.
- `EXExtensionPointIdentifier`: The extension point name for RAW processors. Set to the value for [`kMERAWProcessorExtensionPointName`](kmerawprocessorextensionpointname.md).
- `EXPrincipalClass`: The name of the RAW processor factory class that conforms to the [`MERAWProcessorExtension`](merawprocessorextension.md) protocol.
- [`kMERAWProcessorObjectNameKey`](kmerawprocessorobjectnamekey.md): A user-readable string that describes RAW processor. This string is used for uniquely identifying RAW processors and possibly for debug logging but is typically not visible to users.
- [`kMERAWProcessorProcessorInfoKey`](kmerawprocessorprocessorinfokey.md): An array of one or more dictionaries describing the codecs that the RAW processor supports. Each dictionary must include the following keys: - [`kMERAWProcessorCodecTypeKey`](kmerawprocessorcodectypekey.md): A string describing the four-character code of the codec associated with the video decoder. Each string should be exactly four characters long and use ASCII character set encoding.
- [`kMERAWProcessorCodecNameKey`](kmerawprocessorcodecnamekey.md): A user-readable string describing the name of the codec format. This string might be displayed as format information for the video track in a player application.

## Topics

### Property list keys
- [var kMEVideoDecoderClassImplementationIDKey: String](kmevideodecoderclassimplementationidkey.md)
  The unique identifier for the video decoder.
- [var kMERAWProcessorExtensionPointName: String](kmerawprocessorextensionpointname.md)
  The extension point name for RAW processors.
- [var kMEVideoDecoderObjectNameKey: String](kmevideodecoderobjectnamekey.md)
  A user-readable string describing the decoder.
- [var kMEVideoDecoderCodecInfoKey: String](kmevideodecodercodecinfokey.md)
  An array of one or more dictionaries describing the codecs that the decoder supports.
- [var kMEVideoDecoderCodecTypeKey: String](kmevideodecodercodectypekey.md)
  A string describing the four-character code of the codec that the decoder supports.
- [var kMEVideoDecoderCodecNameKey: String](kmevideodecodercodecnamekey.md)
  A user-readable string describing the name of the codec format.

## See Also

- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/raw-processor-property-list-dictionary)*