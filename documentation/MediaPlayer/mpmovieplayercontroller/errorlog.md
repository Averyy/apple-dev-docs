# errorLog

**Framework**: Media Player  
**Kind**: property

A snapshot of the playback failure error log for the movie player if it is playing a network stream.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var errorLog: MPMovieErrorLog! { get }
```

#### Discussion

Can be `nil`. For information about movie error logs, refer to [`MPMovieErrorLog`](mpmovieerrorlog.md).

## See Also

- [var accessLog: MPMovieAccessLog!](mpmovieplayercontroller/accesslog.md)
  A snapshot of the network playback log for the movie player if it is playing a network stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/errorlog)*