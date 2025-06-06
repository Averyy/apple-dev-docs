# callAsFunction(id:value:)

**Framework**: SwiftUI  
**Kind**: method

Opens a window defined by the window group that presents the specified value type and that’s associated with the specified identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(id: String, value: D) where D : Decodable, D : Encodable, D : Hashable
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`openWindow`](environmentvalues/openwindow.md) action with an identifier and a value:

```swift
openWindow(id: "message", value: message.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `id`: The identifier of the scene to present.
- `value`: The value to present.

## See Also

- [func callAsFunction(id: String)](openwindowaction/callasfunction(id:).md)
  Opens a window that’s associated with the specified identifier.
- [func callAsFunction<D>(value: D)](openwindowaction/callasfunction(value:).md)
  Opens a window defined by a window group that presents the type of the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(id:value:))*