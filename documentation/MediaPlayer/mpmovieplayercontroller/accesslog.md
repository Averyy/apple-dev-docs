# accessLog

**Framework**: Media Player  
**Kind**: property

A snapshot of the network playback log for the movie player if it is playing a network stream.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var accessLog: MPMovieAccessLog! { get }
```

#### Discussion

Can be `nil`. For information about movie access logs, refer to [`MPMovieAccessLog`](mpmovieaccesslog.md).

## See Also

- [var errorLog: MPMovieErrorLog!](mpmovieplayercontroller/errorlog.md)
  A snapshot of the playback failure error log for the movie player if it is playing a network stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/accesslog)*