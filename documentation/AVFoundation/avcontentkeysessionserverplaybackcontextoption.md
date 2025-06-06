# AVContentKeySessionServerPlaybackContextOption

**Framework**: AVFoundation  
**Kind**: struct

Options for specifying additional information for generating server playback context (SPC).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVContentKeySessionServerPlaybackContextOption
```

## Topics

### Server Playback Context Options
- [static let protocolVersions: AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption/protocolversions.md)
  Specifies the versions of the content protection protocols supported by the application.
- [static let serverChallenge: AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption/serverchallenge.md)
  Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.
### Initializing an Options Structure
- [init(rawValue: String)](avcontentkeysessionserverplaybackcontextoption/init(rawvalue:).md)
  Creates a playback context options structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func invalidatePersistableContentKey(Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeysession/invalidatepersistablecontentkey(_:options:completionhandler:).md)
  Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [func invalidateAllPersistableContentKeys(forApp: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeysession/invalidateallpersistablecontentkeys(forapp:options:completionhandler:).md)
  Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption)*