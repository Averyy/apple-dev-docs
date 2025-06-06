# init(_:systemImage:value:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, systemImage: String, value: Value, @ViewBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `titleKey`: The localized string key label for the tab’s tab item.
- `systemImage`: The system image for the tab’s tab item.
- `value`: The   value which selects this tab.
- `content`: The view content of the tab.

## See Also

- [init(_:systemImage:content:)](tab/init(_:systemimage:content:).md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:role:content:)](tab/init(_:systemimage:role:content:).md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:role:content:)](tab/init(_:systemimage:value:role:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:systemimage:value:content:))*