# creationDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A metadata item that indicates the asset’s creation date.

**Availability**:
- iOS 5.0+ - Deprecated in 16.0
- iPadOS 5.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`creationDate`](../avpartialasyncproperty/creationdate.md) asynchronously instead.

## Declaration

```swift
var creationDate: AVMetadataItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVMetadataItem * creationDate;
```

#### Discussion

If the asset contains metadata that the framework can convert to an [`NSDate`](../../Foundation/nsdate.md), you can retrieve it from the metadata item using its [`dateValue`](../avmetadataitem/datevalue.md) property. Otherwise, you retrieve it as a string by using the metadata item’s [`stringValue`](../avmetadataitem/stringvalue.md) property.

This property value is `nil` if no creation date metadata exists.

## See Also

### Accessing metadata
- [metadata](./metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](./commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](./availablemetadataformats.md)
  The metadata formats this asset contains.
- [- metadataForFormat:](./metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [lyrics](./lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/creationdate)*