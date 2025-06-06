# invalidateAllPersistableContentKeys(forApp:options:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.

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
func invalidateAllPersistableContentKeys(forApp appIdentifier: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil) async throws -> Data
```

## Parameters

- `appIdentifier`: An opaque identifier for the app.
- `options`: See   for supported options.
- `handler`: The completion handler callback.

## See Also

- [func invalidatePersistableContentKey(Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeysession/invalidatepersistablecontentkey(_:options:completionhandler:).md)
  Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [struct AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption.md)
  Options for specifying additional information for generating server playback context (SPC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/invalidateallpersistablecontentkeys(forapp:options:completionhandler:))*