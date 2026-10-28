# serverChallenge

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let serverChallenge: AVContentKeySessionServerPlaybackContextOption
```

```c
extern AVContentKeySessionServerPlaybackContextOption const AVContentKeySessionServerPlaybackContextOptionServerChallenge;
```

## Discussion

Specify this value as an 8-byte [`NSData`](../../Foundation/nsdata.md) object. If you don’t specify a value for this key, the system assumes a default server challenge of `0`.

## See Also

### Server playback context options
- [static let protocolVersions: AVContentKeySessionServerPlaybackContextOption](./protocolversions.md)
  Specifies the versions of the content protection protocols supported by the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/serverchallenge)*