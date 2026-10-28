# init(_:for:content:defaultValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a data-presenting window group with a localized title string and a default value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init<D, C>(_ titleResource: LocalizedStringResource, for type: D.Type = D.self, @ContentBuilder content: @escaping (Binding<D>) -> C, defaultValue: @escaping () -> D) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init<D, C>(_ title: Text, for type: D.Type = D.self, @ContentBuilder content: @escaping (Binding<D>) -> C, defaultValue: @escaping () -> D) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

```swift
nonisolated
init<D, C>(_ titleKey: LocalizedStringKey, for type: D.Type = D.self, @ContentBuilder content: @escaping (Binding<D>) -> C, defaultValue: @escaping () -> D) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

```swift
nonisolated
init<S, D, C>(_ title: S, for type: D.Type = D.self, @ContentBuilder content: @escaping (Binding<D>) -> C, defaultValue: @escaping () -> D) where Content == PresentedWindowContent<D, C>, S : StringProtocol, D : Decodable, D : Encodable, D : Hashable, C : View
```

## Discussion

The window group uses the specified content as a template to create each window in the group.

The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

SwiftUI creates a window from the group when you present a value of the specified type using the [`openWindow`](../environmentvalues/openwindow.md) action.

## Parameters

- `titleResource`: The title key to use for the group’s title.
- `type`: The type of presented data this window group accepts.
- `content`: A closure that creates the content for each instance of the group. The closure receives a binding to the value that you pass into the [`openWindow`](../environmentvalues/openwindow.md) action when you open the window. SwiftUI automatically persists and restores the value of this binding as part of the state restoration process.
- `defaultValue`: A closure that returns a default value to present. SwiftUI calls this closure when it has no data to provide, like when someone opens a new window from the File > New Window menu item.

## See Also

### Providing default data to a window group
- [init<D, C>(for: D.Type, content: (Binding<D>) -> C, defaultValue: () -> D)](./init%28for,content,defaultvalue%29.md)
  Creates a data-presenting window group with a default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(_:for:content:defaultvalue:))*