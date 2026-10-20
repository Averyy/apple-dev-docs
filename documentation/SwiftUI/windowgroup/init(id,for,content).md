# init(id:for:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a data-presenting window group with an identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<D, C>(id: String, for type: D.Type, @ContentBuilder content: @escaping (Binding<D?>) -> C) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

Available when `Content` conforms to `View`.

#### Discussion

The window group uses the specified content as a template to create each window in the group.

SwiftUI creates a window from the group when you present a value of the specified type using the [`openWindow`](../environmentvalues/openwindow.md) action.

## Parameters

- `id`: A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.
- `type`: The type of presented data this window group accepts.
- `content`: A closure that creates the content for each instance of the group. The closure receives a binding to the value that you pass into the [`openWindow`](../environmentvalues/openwindow.md) action when you open the window. SwiftUI automatically persists and restores the value of this binding as part of the state restoration process.

## See Also

### Identifying a data-driven window group
- [init(_:id:for:content:)](./init%28_,id,for,content%29.md)
  Creates a data-presenting window group with a localized title string and an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(id:for:content:))*