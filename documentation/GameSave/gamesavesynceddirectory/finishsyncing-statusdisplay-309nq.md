# finishSyncing(statusDisplay:)

**Framework**: GameSave  
**Kind**: method

Waits for the directory sync to complete, showing the sync’s progress in a modal alert.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func finishSyncing(statusDisplay window: NSWindow) async
```

#### Discussion

If the sync results in a conflict, the framework displays a conflict resolution UI for the user to chose a version that will be used. If the user isn’t signed in to iCloud or iCloud drive, the framework informs the user and then switches to local saving.

## Parameters

- `window`: The window where the system shows progress and alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/finishsyncing(statusdisplay:)-309nq)*