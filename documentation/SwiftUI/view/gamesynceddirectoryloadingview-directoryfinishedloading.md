# gameSyncedDirectoryLoadingView(directory:finishedLoading:)

**Framework**: SwiftUI  
**Kind**: method

Presents a modal view while the game synced directory loads.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func gameSyncedDirectoryLoadingView(directory: Binding<GameSyncedDirectory?>, finishedLoading: @escaping @MainActor () -> Void) -> some View
```

#### Discussion

Use this method when you want to present a modal loading view to the user when a Boolean value you provide is true.

## Parameters

- `directory`: A binding to an optional game synced directory that was returned by calling  .   If this value is  , the view doesn’t display.
- `finishedLoading`: The closure to execute after the loading process completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gamesynceddirectoryloadingview(directory:finishedloading:))*