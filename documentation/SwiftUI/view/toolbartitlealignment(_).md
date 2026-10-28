# toolbarTitleAlignment(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the preferred alignment of the navigation bar’s title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+

## Declaration

```swift
nonisolated
func toolbarTitleAlignment(_ alignment: ToolbarTitleAlignment) -> some View
```

## Discussion

The navigation bar resolves the alignment of its title automatically based on context, and toolbar roles. Use this modifier to override that resolution.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Library")
        .toolbarTitleAlignment(.center)
}
```

## Parameters

- `alignment`: The preferred navigation title alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbartitlealignment(_:))*