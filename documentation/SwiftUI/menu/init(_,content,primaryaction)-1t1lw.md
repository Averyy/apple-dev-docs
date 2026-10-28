# init(_:content:primaryAction:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a menu with a custom primary action that generates its label from a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text, S : StringProtocol
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content, primaryAction: @escaping () -> Void) where Label == Text
```

## Discussion

To create the label with a localized string key, use `Menu(_:primaryAction:content:)` instead.

## Parameters

- `title`: A string that describes the contents of the menu.
- `content`: A group of menu items.
- `primaryAction`: The action to perform on primary interaction with the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menu/init(_:content:primaryaction:)-1t1lw)*