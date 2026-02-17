# init(propertiesOf:valueLoadingHandler:)

**Framework**: AVFoundation  
**Kind**: init

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(propertiesOf metadataItem: AVMetadataItem, valueLoadingHandler handler: @escaping @Sendable (AVMetadataItemValueRequest) -> Void)
```

#### Return Value

An instance of AVMetadataItem.

#### Discussion

Creates an instance of AVMutableMetadataItem with a value that you do not wish to load unless required, e.g. a large image value that needn’t be loaded into memory until another module wants to display it.

This method is intended for the creation of metadata items for optional display purposes, when there is no immediate need to load specific metadata values. For example, see the interface for navigation markers as consumed by AVPlayerViewController. It’s not intended for the creation of metadata items with values that are required immediately, such as metadata items that are provided for impending serialization operations (e.g. via -[AVAssetExportSession setMetadata:] and other similar methods defined on AVAssetWriter and AVAssetWriterInput). When -loadValuesAsynchronouslyForKeys:completionHandler: is invoked on an AVMetadataItem created via +metadataItemWithPropertiesOfMetadataItem:valueLoadingHandler: and @“value” is among the keys for which loading is requested, the block you provide as the value loading handler will be executed on an arbitrary dispatch queue, off the main thread. The handler can perform I/O and other necessary operations to obtain the value. If loading of the value succeeds, provide the value by invoking -[AVMetadataItemValueRequest respondWithValue:]. If loading of the value fails, provide an instance of NSError that describes the failure by invoking -[AVMetadataItemValueRequest respondWithError:].

## Parameters

- `metadataItem`: An instance of AVMetadataItem with the identifier, extendedLanguageTag, and other property values that you want the newly created instance of AVMetadataItem to share. The value of metadataItem is ignored.
- `handler`: A block that loads the value of the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/init(propertiesof:valueloadinghandler:))*