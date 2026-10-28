# init(_:image:role:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab that you can use in a tab view, with a localized string resource.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ titleResource: LocalizedStringResource, image: String, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

Available when `Value` is `Never`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
init(_ titleKey: LocalizedStringKey, image: String, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
init<S>(_ title: S, image: String, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

## Parameters

- `titleResource`: The localized string resource label for the tab’s tab item.
- `image`: The image for the tab’s tab item.
- `role`: The role defining the semantic purpose of the tab.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:image:role:content:)-76tyh)*