# init(_:image:role:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new tab that you can use in a tab view, with a localized string key label.

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
init(_ titleKey: LocalizedStringKey, image: String, role: TabRole?, @ViewBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `titleKey`: The localized string key label for the tab’s tab item.
- `image`: The image for the tab’s tab item.
- `role`: The role defining the semantic purpose of the tab.
- `content`: The view content of the tab.

## See Also

- [init(_:image:content:)](tab/init(_:image:content:).md)
  Creates a new tab that you can use in a tab view, with a localized string key label.
- [init(_:image:value:content:)](tab/init(_:image:value:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.
- [init(_:image:value:role:content:)](tab/init(_:image:value:role:content:).md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:image:role:content:))*