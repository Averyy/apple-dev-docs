# metadataForSidecarFile

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 26.0+

## Declaration

```swift
optional var metadataForSidecarFile: Data { get }
```

```objc
@property (readonly) NSData * metadataForSidecarFile;
```

## Discussion

The metadata returned is a pre-formatted NSData that represents a fully-formed sidecar file, and should be compatible with the MediaExtension FormatReader.

The metadata will contain the initial processing parameters from the sidecar file, along with any adjustments made on the RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/metadataforsidecarfile)*