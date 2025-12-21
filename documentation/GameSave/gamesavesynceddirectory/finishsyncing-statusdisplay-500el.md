# finishSyncing(statusDisplay:)

**Framework**: GameSave  
**Kind**: method

Waits for the directory sync to complete, showing the sync’s progress in a modal alert.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finishSyncing(statusDisplay window: UIWindow) async
```

#### Discussion

If the sync results in a conflict, the framework displays a conflict resolution UI for the user to chose a version that will be used. If the user isn’t signed in to iCloud or iCloud drive, the framework informs the user and then switches to local saving.

## Parameters

- `window`: The window where the system shows progress and alerts.

## See Also

- [func finishSyncing() async](gamesavesynceddirectory/finishsyncing.md)
  Waits for the directory sync to complete, without showing any user interface.
- [func finishSyncing(statusDisplay: NSWindow) async](gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq.md)
  Waits for the directory sync to complete, showing the sync’s progress in a modal alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/finishsyncing(statusdisplay:)-500el)*