# init(url:options:)

**Framework**: AVFoundation  
**Kind**: init

Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(url URL: URL, options: [String : Any]? = nil)
```

#### Discussion

Upon creation, the values of the [`defaultMediaDataStorage`](avmovie/defaultmediadatastorage.md) property and any associated [`mediaDataStorage`](avmovietrack/mediadatastorage.md) properties are `nil`.

## Parameters

- `URL`: A URL that points to a file containing a movie header.
- `options`: A dictionary of options to use to initialize the movie.

## See Also

- [convenience init(url: URL)](avmovie/init(url:).md)
  Creates a movie that models the media at the specified URL.
- [init(data: Data, options: [String : Any]?)](avmovie/init(data:options:).md)
  Creates a movie object from a movie file’s data.
- [Initialization Options](initialization-options.md)
  Specify options to configure the initialization of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/init(url:options:))*