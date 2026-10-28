# movieWithData:options:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new movie object from a movie file’s data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) movieWithData:(NSData *) data options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A movie object.

## Discussion

Use this method to create movies from movie headers that aren’t stored in files, which can include movies that the pasteboard contains.

## Parameters

- `data`: A data object that contains a movie header.
- `options`: A dictionary of options to use to initialize the movie.

## See Also

### Creating a movie
- [+ movieWithURL:options:](./moviewithurl_options_.md)
  Returns a new movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(url: URL, options: [String : Any]?)](./init%28url,options%29-1wjrq.md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](./init%28data,options%29.md)
  Creates a movie object from a movie file’s data.
- [Initialization options](../initialization-options.md)
  Specify options to configure the initialization of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/moviewithdata:options:)*