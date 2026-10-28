# assetReaderWithAsset:error:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new object to read media data from an asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetReaderWithAsset:(AVAsset *) asset error:(NSError **) outError;
```

## Return Value

A new asset reader object.

## Parameters

- `asset`: The asset from which to read media data.
- `outError`: On return, if the initialization fails, a pointer to an error object provides the details of the failure.

## See Also

### Creating an asset reader
- [init(asset: AVAsset) throws](./init%28asset%29.md)
  Creates an object to read media data from an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/assetreaderwithasset:error:)*