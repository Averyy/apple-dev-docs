# init(url:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a movie that models the media at the specified URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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

### Creating a movie
- [init(url: URL, options: [String : Any]?)](./init%28url,options%29-1wjrq.md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](./init%28data,options%29.md)
  Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md)
  Specify options to configure the initialization of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/init(url:))*