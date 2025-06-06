# draggable(_:)

**Framework**: SwiftUI  
**Kind**: method

Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+

## Declaration

```swift
@MainActor
@preconcurrency func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some TabContent<Self.TabValue> where T : Transferable
```

#### Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this tab. When a drag operation begins, a rendering of the tab is generated and used as the preview image.

The following example allows the ‘Family’ tab to be dragged and dropped.

```swift
TabView {
    Tab("Family", systemImage: "list.bullet") {
        MyFamilyView()
    }
    .draggable(AppSections.family)
}
```

## Parameters

- `payload`: A closure that returns a single   instance or a value conforming to   that   represents the draggable data from this tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/draggable(_:))*