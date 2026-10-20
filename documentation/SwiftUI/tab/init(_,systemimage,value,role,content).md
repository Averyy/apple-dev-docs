# init(_:systemImage:value:role:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(_ titleKey: LocalizedStringKey, systemImage: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, systemImage: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
nonisolated
init<S, T>(_ title: S, systemImage: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, S : StringProtocol, T : Hashable
```

```swift
nonisolated
init<S>(_ title: S, systemImage: String, value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

```swift
nonisolated
init<T>(_ titleKey: LocalizedStringKey, systemImage: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

```swift
nonisolated
init<T>(_ titleResource: LocalizedStringResource, systemImage: String, value: T, role: TabRole?, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

## Parameters

- `titleKey`: The localized string key label for the tab’s tab item.
- `systemImage`: The system image for the tab’s tab item.
- `value`: The `selection` value which selects this tab.
- `role`: The role defining the semantic purpose of the tab.
- `content`: The view content of the tab.

## See Also

### Creating a tab with system symbol
- [init(_:systemImage:content:)](./init%28_,systemimage,content%29.md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:content:)](./init%28_,systemimage,value,content%29.md)
  Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
- [init(_:systemImage:role:content:)](./init%28_,systemimage,role,content%29.md)
  Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:systemimage:value:role:content:))*