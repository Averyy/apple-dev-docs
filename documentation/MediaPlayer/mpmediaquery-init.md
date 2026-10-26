# init

**Framework**: Media Player  
**Role**: Article

Initializes a generic media query.

#### Return Value

A query containing everything in the user’s Music library.

#### Overview

A generic media query has no filter predicates and no grouping configuration. It matches everything in the Music library and provides no grouping or sorting.

## See Also

### Creating media queries
- [class func albums() -> MPMediaQuery](./mpmediaquery/albums%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by album name.
- [class func artists() -> MPMediaQuery](./mpmediaquery/artists%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by artist name.
- [class func songs() -> MPMediaQuery](./mpmediaquery/songs%28%29.md)
  Creates a media query that matches music items and that groups and sorts collections by song name.
- [class func playlists() -> MPMediaQuery](./mpmediaquery/playlists%28%29.md)
  Creates a media query that matches the entire library and that groups and sorts collections by playlist name.
- [class func podcasts() -> MPMediaQuery](./mpmediaquery/podcasts%28%29.md)
  Creates a media query that matches podcast items and that groups and sorts collections by podcast name.
- [class func audiobooks() -> MPMediaQuery](./mpmediaquery/audiobooks%28%29.md)
  Creates a media query that matches audio book items and that groups and sorts collections by audio book name.
- [class func compilations() -> MPMediaQuery](./mpmediaquery/compilations%28%29.md)
  Creates a media query that matches compilation items and that groups and sorts collections by album name.
- [class func composers() -> MPMediaQuery](./mpmediaquery/composers%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by composer name.
- [class func genres() -> MPMediaQuery](./mpmediaquery/genres%28%29.md)
  Creates a media query that matches all media items and that groups and sorts collections by genre name.
- [init(filterPredicates: Set<MPMediaPredicate>?)](./mpmediaquery/init%28filterpredicates%29.md)
  Initializes a media query with a set of media property predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaquery-init)*