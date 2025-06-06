# init(data:options:)

**Framework**: AVFoundation  
**Kind**: init

Creates a movie object from a movie file’s data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(data: Data, options: [String : Any]? = nil)
```

#### Discussion

Use this method to create movies from movie headers that aren’t stored in files, which can include movies that the pasteboard contains.

## Parameters

- `data`: A data object that contains a movie header.
- `options`: A dictionary of options to use to initialize the movie.

## See Also

- [convenience init(url: URL)](avmovie/init(url:).md)
  Creates a movie that models the media at the specified URL.
- [init(url: URL, options: [String : Any]?)](avmovie/init(url:options:).md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [Initialization Options](initialization-options.md)
  Specify options to configure the initialization of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/init(data:options:))*