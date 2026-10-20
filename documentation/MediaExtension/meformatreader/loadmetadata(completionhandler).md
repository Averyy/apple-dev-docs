# loadMetadata(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Loads the array of metadata items from the media asset.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func loadMetadata(completionHandler: @escaping @Sendable ([AVMetadataItem]?, (any Error)?) -> Void)
```

```swift
func metadata() async throws -> [AVMetadataItem]
```

```objc
- (void) loadMetadataWithCompletionHandler:(void (^)(NSArray<AVMetadataItem *> *metadata, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The completion block to execute when the load operation finishes.

## See Also

### Reading and parsing media assets
- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](./loadfileinfo%28completionhandler%29.md)
  Loads the file info object with the properties of the media asset.
- [func loadTrackReaders(completionHandler: ([any METrackReader]?, (any Error)?) -> Void)](./loadtrackreaders%28completionhandler%29.md)
  Loads the array of track readers that represent the tracks in the media asset.
- [func parseAdditionalFragments(completionHandler: (MEFormatReaderParseAdditionalFragmentsStatus, (any Error)?) -> Void)](./parseadditionalfragments%28completionhandler%29.md)
  Incorporates additional fragments that the file received after the last time the format reader parsed it.
- [struct MEFormatReaderParseAdditionalFragmentsStatus](../meformatreaderparseadditionalfragmentsstatus.md)
  Informational status flags that the format reader returns after parsing additional fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreader/loadmetadata(completionhandler:))*