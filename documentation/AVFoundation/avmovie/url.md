# url

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A URL to a QuickTime or ISO base media file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var url: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * URL;
```

#### Discussion

The value is `nil` if you didn’t initialize the movie with a URL.

## See Also

### Accessing movie information
- [var data: Data?](./data.md)
  A data object that contains the movie file’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/url)*