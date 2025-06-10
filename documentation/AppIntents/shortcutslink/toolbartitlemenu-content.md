# toolbarTitleMenu(content:)

**Framework**: App Intents  
**Kind**: method

Configure the title menu of a toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarTitleMenu<C>(@ViewBuilder content: () -> C) -> some View where C : View
```

#### Discussion

A title menu represent common functionality that can be done on the content represented by your app’s toolbar or navigation title. This menu may be populated from your app’s commands like `CommandGroupPlacement/saveItem` or `CommandGroupPlacement/printItem`.

```swift
ContentView()
    .toolbar {
        ToolbarTitleMenu()
    }
```

You can provide your own set of actions to override this behavior.

```swift
ContentView()
    .toolbarTitleMenu {
        DuplicateButton()
        PrintButton()
    }
```

In iOS and iPadOS, this will construct a menu that can be presented by tapping the navigation title in the app’s navigation bar.

## Parameters

- `content`: The content associated to the toolbar title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/toolbartitlemenu(content:))*