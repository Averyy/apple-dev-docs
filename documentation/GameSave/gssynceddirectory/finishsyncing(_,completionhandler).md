# finishSyncing(_:completionHandler:)

**Framework**: GameSave  
**Kind**: method  
**Role**: Instance Method

Waits for the directory sync to complete, showing the sync’s progress in a modal alert.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func finishSyncing(_ statusDisplay: UIWindow, completionHandler completion: @escaping @Sendable () -> Void)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func finishSyncing(_ statusDisplay: UIWindow) async
```

*macOS*

```swift
func finishSyncing(_ statusDisplay: NSWindow, completionHandler completion: @escaping @Sendable () -> Void)
```

*macOS*

```swift
func finishSyncing(_ statusDisplay: NSWindow) async
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) finishSyncing:(UIWindow *) statusDisplay completionHandler:(void (^)()) completion;
```

*macOS*

```objc
- (void) finishSyncing:(NSWindow *) statusDisplay completionHandler:(void (^)()) completion;
```

## Discussion

If the sync results in a conflict, the framework displays a conflict resolution UI for the user to chose a version that will be used. If the user isn’t signed in to iCloud or iCloud drive, the framework informs the user and then switches to local saving.

## Parameters

- `statusDisplay`: The window where the system shows progress and alerts.
- `completion`: The block that GameSave calls after syncing finishes.

## See Also

### Syncing a directory
- [func finishSyncing(completionHandler: () -> Void)](./finishsyncing%28completionhandler%29.md)
  Waits for the directory sync to complete, without showing any user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/finishsyncing(_:completionhandler:))*