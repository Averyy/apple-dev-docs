# querySignature

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

The query signature for the match.

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
var querySignature: SHSignature { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly) SHSignature * querySignature;
```

*macOS*

```objc
@property (atomic, strong, readonly) SHSignature * querySignature;
```

## See Also

### Reading match information
- [var mediaItems: [SHMatchedMediaItem]](./mediaitems.md)
  An array of the media items in the catalog that match the query signature, in order of the quality of the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmatch/querysignature)*