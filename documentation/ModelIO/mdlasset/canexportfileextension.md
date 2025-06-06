# canExportFileExtension(_:)

**Framework**: Model I/O  
**Kind**: method

Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can write asset data as a file with the specified format extension.

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the [`MDLAsset`](mdlasset.md) class can export asset data in the format with the specified extension; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), you can use the [`export(to:)`](mdlasset/export(to:).md) method to write an asset to a file using the format identified by the specified extension.

The set of supported formats includes Wavefront Object (`.obj`) and Standard Tessellation Language (`.stl`). Additional formats may be supported as well.

## Parameters

- `extension`: The filename extension identifying an asset file format.

## See Also

- [func export(to: URL) throws](mdlasset/export(to:).md)
  Writes asset data to a file at the specified URL and reports errors that occur during export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/canexportfileextension(_:))*