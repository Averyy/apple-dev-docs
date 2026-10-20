# finishSyncing()

**Framework**: GameSave  
**Kind**: method  
**Role**: Instance Method

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

### Syncing a directory
- [func finishSyncing(statusDisplay: NSWindow) async](./finishsyncing%28statusdisplay%29-309nq.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.
- [func finishSyncing(statusDisplay: UIWindow) async](./finishsyncing%28statusdisplay%29-500el.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/finishsyncing())*