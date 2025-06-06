# protocolVersions

**Framework**: AVFoundation  
**Kind**: property

Specifies the versions of the content protection protocols supported by the application.

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
static let protocolVersions: AVContentKeySessionServerPlaybackContextOption
```

#### Discussion

If you don’t specify a value for this key, the system assumes a default protocol version of `1`.

## See Also

- [static let serverChallenge: AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption/serverchallenge.md)
  Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption/protocolversions)*