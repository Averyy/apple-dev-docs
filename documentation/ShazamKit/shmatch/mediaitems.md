# mediaItems

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

An array of the media items in the catalog that match the query signature, in order of the quality of the match.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var mediaItems: [SHMatchedMediaItem] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly) NSArray<SHMatchedMediaItem *> * mediaItems;
```

*macOS*

```objc
@property (atomic, strong, readonly) NSArray<SHMatchedMediaItem *> * mediaItems;
```

## See Also

### Reading match information
- [var querySignature: SHSignature](./querysignature.md)
  The query signature for the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatch/mediaitems)*