# init(_:image:value:role:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a localized string key label.

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
nonisolated
init(_ titleResource: LocalizedStringResource, image: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
nonisolated
init<S, T>(_ title: S, image: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, S : StringProtocol, T : Hashable
```

```swift
nonisolated
init<S>(_ title: S, image: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

```swift
nonisolated
init<T>(_ titleKey: LocalizedStringKey, image: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

```swift
nonisolated
init<T>(_ titleResource: LocalizedStringResource, image: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

## Parameters

- `titleResource`: The localized string resource label for the tab’s tab item.
- `image`: The image for the tab’s tab item.
- `value`: The `selection` value which selects this tab.
- `role`: The role defining the semantic purpose of the tab.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:image:value:role:content:)-7jp42)*