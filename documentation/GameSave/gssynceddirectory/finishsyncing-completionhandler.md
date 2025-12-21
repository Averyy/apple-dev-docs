# finishSyncing(completionHandler:)

**Framework**: GameSave  
**Kind**: method

Waits for the directory sync to complete, without showing any user interface.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finishSyncing() async
```

#### Discussion

Use this method to wait if your app displays its own syncing UI.

## See Also

- [func finishSyncing(UIWindow, completionHandler: () -> Void)](gssynceddirectory/finishsyncing(_:completionhandler:).md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/finishsyncing(completionhandler:))*