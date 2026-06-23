# documentBrowserContextMenu(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds to a `DocumentGroupLaunchScene` actions that accept a list of selected files as their parameter.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func documentBrowserContextMenu(@ContentBuilder _ menu: @escaping ([URL]?) -> some View) -> some Scene
```

#### Discussion

The actions are displayed in the document browser navigation bar when a document browser is in Select mode, and also added to context menu for the file items.

## Parameters

- `menu`: Items representing the content of the menu.

## See Also

- [func documentLaunchTitle(_:)](scene/documentlaunchtitle(_:).md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](scene/documentlaunchsubtitle(_:).md)
  Sets the subtitle displayed beneath the title on the document launch card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/documentbrowsercontextmenu(_:))*