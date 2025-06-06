# init(url:)

**Framework**: AVFoundation  
**Kind**: init

Creates a movie that models the media at the specified URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(url: URL)
```

## Parameters

- `url`: A URL to a local, remote, or HTTP Live Streaming media resource.

## See Also

- [init(url: URL, options: [String : Any]?)](avmovie/init(url:options:).md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](avmovie/init(data:options:).md)
  Creates a movie object from a movie file’s data.
- [Initialization Options](initialization-options.md)
  Specify options to configure the initialization of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/init(url:))*