# exportAssetToURL:

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Writes asset data to a file at the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) exportAssetToURL:(NSURL *) URL;
```

#### Return Value

[`true`](../../Swift/true.md) if export succeeded; otherwise, [`false`](../../Swift/false.md).

#### Discussion

For best results, use the [`export(to:)`](./export%28to%29.md) method so that you can respond to possible errors during export.

The [`MDLAsset`](../mdlasset.md) class infers the data format to export in from the [`pathExtension`](../../Foundation/nsurl/pathextension.md) property of the specified URL. To determine whether a format is supported for export, call the [`canExportFileExtension(_:)`](./canexportfileextension%28_%29.md) method.

## Parameters

- `URL`: A URL specifying the location to export asset data to. This parameter must be a `file:` URL.

## See Also

### Exporting an Asset
- [class func canExportFileExtension(String) -> Bool](./canexportfileextension%28_%29.md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](../mdlasset.md) class can write asset data as a file with the specified format extension.
- [func export(to: URL) throws](./export%28to%29.md)
  Writes asset data to a file at the specified URL and reports errors that occur during export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/exportassettourl:)*