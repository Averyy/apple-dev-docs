# export(to:)

**Framework**: Model I/O  
**Kind**: method

Writes asset data to a file at the specified URL and reports errors that occur during export.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func export(to URL: URL) throws
```

#### Discussion

The [`MDLAsset`](mdlasset.md) class infers the data format to export in from the [`pathExtension`](https://developer.apple.com/documentation/foundation/nsurl/1410208-pathextension) property of the specified URL. To determine whether a format is supported for export, call the [`canExportFileExtension(_:)`](mdlasset/canexportfileextension(_:).md) method.

## Parameters

- `URL`: A URL specifying the location to export asset data to. This parameter must be a   URL.

## See Also

- [class func canExportFileExtension(String) -> Bool](mdlasset/canexportfileextension(_:).md)
  Returns a Boolean value that indicates whether the [`MDLAsset`](mdlasset.md) class can write asset data as a file with the specified format extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/export(to:))*