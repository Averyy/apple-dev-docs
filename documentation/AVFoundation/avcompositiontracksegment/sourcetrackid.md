# sourceTrackID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An identifier of a track in the container file whose media this track segment presents.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var sourceTrackID: CMPersistentTrackID { get }
```

```objc
@property (nonatomic, readonly) CMPersistentTrackID sourceTrackID;
```

## See Also

### Accessing segment properties
- [var sourceURL: URL?](./sourceurl.md)
  A URL of the container file whose media this track segment presents.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the segment is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontracksegment/sourcetrackid)*