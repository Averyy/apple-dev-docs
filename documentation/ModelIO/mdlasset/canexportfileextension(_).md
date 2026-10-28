# canExportFileExtension(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the [`MDLAsset`](../mdlasset.md) class can write asset data as a file with the specified format extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func canExportFileExtension(_ extension: String) -> Bool
```

```objc
+ (BOOL) canExportFileExtension:(NSString *) extension;
```

## Return Value

[`true`](../../Swift/true.md) if the [`MDLAsset`](../mdlasset.md) class can export asset data in the format with the specified extension; otherwise, [`false`](../../Swift/false.md).

## Discussion

If this method returns [`true`](../../Swift/true.md), you can use the [`export(to:)`](./export%28to%29.md) method to write an asset to a file using the format identified by the specified extension.

The set of supported formats includes Wavefront Object (`.obj`) and Standard Tessellation Language (`.stl`). Additional formats may be supported as well.

## Parameters

- `extension`: The filename extension identifying an asset file format.

## See Also

### Exporting an Asset
- [func export(to: URL) throws](./export%28to%29.md)
  Writes asset data to a file at the specified URL and reports errors that occur during export.
- [- exportAssetToURL:](./exportassettourl_.md)
  Writes asset data to a file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/canexportfileextension(_:))*