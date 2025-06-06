# serverChallenge

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

Specify this value as an 8-byte [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object. If you don’t specify a value for this key, the system assumes a default server challenge of `0`.

## See Also

- [static let protocolVersions: AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption/protocolversions.md)
  Specifies the versions of the content protection protocols supported by the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/serverchallenge)*