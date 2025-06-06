# UnderlyingError

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that describes a system framework error.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object UnderlyingError
```

#### Discussion

The client depends on a number of system frameworks that manage user interaction and media playback, each of which can generate its own errors. For example, if your service provides a [`Content`](content.md) object that contains a malformed or expired URL, the [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) framework generates an error when it attempts to load that URL. The client uses this object to provide details of the framework error when it reports the playback failure to your service. For more information, see [`Recover from Content Playback Failure`](contentplaybackfailure.md).

An error code is unique only within its associated error domain. Therefore, use `errorDomain` to determine the origin of the error on the client, and then use `errorCode` to identify the specific error within that domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/underlyingerror)*