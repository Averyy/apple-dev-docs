# Initialization options

**Framework**: AVFoundation  
**Role**: API Collection

Specify options to configure the initialization of a movie.

## Topics

### Options
- [let AVMovieReferenceRestrictionsKey: String](./avmoviereferencerestrictionskey.md)
  A key that specifies restrictions for a movie to use when it resolves references to external media data.
- [let AVMovieShouldSupportAliasDataReferencesKey: String](./avmovieshouldsupportaliasdatareferenceskey.md)
  A key that specifies a Boolean value that indicates whether the system parses and resolves alias data references in the movie.

## See Also

### Creating a movie
- [convenience init(url: URL)](./avmovie/init%28url%29.md)
  Creates a movie that models the media at the specified URL.
- [init(url: URL, options: [String : Any]?)](./avmovie/init%28url,options%29-1wjrq.md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](./avmovie/init%28data,options%29.md)
  Creates a movie object from a movie file’s data.
- [+ movieWithURL:options:](./avmovie/moviewithurl_options_.md)
  Returns a new movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [+ movieWithData:options:](./avmovie/moviewithdata_options_.md)
  Returns a new movie object from a movie file’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/initialization-options)*