# init(url:options:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

#### Discussion

Upon creation, the values of the [`defaultMediaDataStorage`](./defaultmediadatastorage.md) property and any associated [`mediaDataStorage`](../avmovietrack/mediadatastorage.md) properties are `nil`.

## Parameters

- `URL`: A URL that points to a file containing a movie header.
- `options`: A dictionary of options to use to initialize the movie.

## See Also

### Creating a movie
- [convenience init(url: URL)](./init%28url%29.md)
  Creates a movie that models the media at the specified URL.
- [init(data: Data, options: [String : Any]?)](./init%28data,options%29.md)
  Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md)
  Specify options to configure the initialization of a movie.
- [+ movieWithURL:options:](./moviewithurl_options_.md)
  Returns a new movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [+ movieWithData:options:](./moviewithdata_options_.md)
  Returns a new movie object from a movie file’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/init(url:options:)-1wjrq)*