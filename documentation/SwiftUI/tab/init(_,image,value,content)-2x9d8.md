# init(_:image:value:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value, with a string label.

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
init<S>(_ title: S, image: String, value: Value, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel, S : StringProtocol
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, image: String, value: Value, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
nonisolated
init(_ titleResource: LocalizedStringResource, image: String, value: Value, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

```swift
nonisolated
init<S, T>(_ title: S, image: String, value: T, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, S : StringProtocol, T : Hashable
```

```swift
nonisolated
init<T>(_ titleKey: LocalizedStringKey, image: String, value: T, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

```swift
nonisolated
init<T>(_ titleResource: LocalizedStringResource, image: String, value: T, @ContentBuilder content: () -> Content) where Value == T?, Label == DefaultTabLabel, T : Hashable
```

## Parameters

- `title`: The label for the tab’s tab item.
- `image`: The image for the tab’s tab item.
- `value`: The `selection` value which selects this tab.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(_:image:value:content:)-2x9d8)*