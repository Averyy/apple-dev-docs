# invalidatePersistableContentKey(_:options:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.

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
func invalidatePersistableContentKey(_ persistableContentKeyData: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil) async throws -> Data
```

## Parameters

- `persistableContentKeyData`: The persistable content key data to invalidate.
- `options`: Additional options to use when generating the server playback context. Pass   to indicate no additional options.
- `handler`: The completion handler callback.

## See Also

- [func invalidateAllPersistableContentKeys(forApp: Data, options: [AVContentKeySessionServerPlaybackContextOption : Any]?, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeysession/invalidateallpersistablecontentkeys(forapp:options:completionhandler:).md)
  Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [struct AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption.md)
  Options for specifying additional information for generating server playback context (SPC).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/invalidatepersistablecontentkey(_:options:completionhandler:))*