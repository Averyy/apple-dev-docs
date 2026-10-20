# AVContentKeySessionServerPlaybackContextOption

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Options for specifying additional information for generating server playback context (SPC).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVContentKeySessionServerPlaybackContextOption
```

```c
typedef NSString * AVContentKeySessionServerPlaybackContextOption;
```

## Topics

### Server playback context options
- [static let protocolVersions: AVContentKeySessionServerPlaybackContextOption](./avcontentkeysessionserverplaybackcontextoption/protocolversions.md)
  Specifies the versions of the content protection protocols supported by the application.
- [static let serverChallenge: AVContentKeySessionServerPlaybackContextOption](./avcontentkeysessionserverplaybackcontextoption/serverchallenge.md)
  Specifies a nonce to include in the secure server playback context (SPC) to prevent replay attacks.
### Initializing an options structure
- [init(rawValue: String)](./avcontentkeysessionserverplaybackcontextoption/init%28rawvalue%29.md)
  Creates a playback context options structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Invalidating content keys
- [func invalidatePersistableContentKey(Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeysession/invalidatepersistablecontentkey%28_,options,completionhandler%29.md)
  Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [func invalidateAllPersistableContentKeys(forApp: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](./avcontentkeysession/invalidateallpersistablecontentkeys%28forapp,options,completionhandler%29.md)
  Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessionserverplaybackcontextoption)*