# serializeAsArchiveAndFlush(url:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Serializes a pipeline data set to an archive.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func serializeAsArchiveAndFlush(url: URL) throws
```

```objc
- (BOOL) serializeAsArchiveAndFlushToURL:(NSURL *) url error:(NSError **) error;
```

## Parameters

- `url`: The URL used to serialize the serializer data set as an archive to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializer/serializeasarchiveandflush(url:))*