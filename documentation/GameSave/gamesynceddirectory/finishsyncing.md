# finishSyncing()

**Framework**: GameSave  
**Kind**: method

Waits for the directory sync to complete, without showing any user interface.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func finishSyncing() async
```

#### Discussion

Use this method to wait if your app displays its own syncing UI.

## See Also

- [func finishSyncing(statusDisplay: NSWindow) async](gamesynceddirectory/finishsyncing(statusdisplay:)-2uvh2.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](gamesynceddirectory/finishsyncing(statusdisplay:)-6v7lz.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/finishsyncing())*