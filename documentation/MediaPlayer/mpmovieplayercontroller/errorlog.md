# errorLog

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A snapshot of the playback failure error log for the movie player if it is playing a network stream.

**Availability**:
- iOS 4.3+ - Deprecated in 9.0
- iPadOS 4.3+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVFoundation.

## Declaration

```swift
var errorLog: MPMovieErrorLog! { get }
```

```objc
@property (nonatomic, readonly) MPMovieErrorLog * errorLog;
```

## Discussion

Can be `nil`. For information about movie error logs, refer to [`MPMovieErrorLog`](../mpmovieerrorlog.md).

## See Also

### Retrieving movie logs
- [var accessLog: MPMovieAccessLog!](./accesslog.md)
  A snapshot of the network playback log for the movie player if it is playing a network stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/errorlog)*