# callAsFunction(value:)

**Framework**: SwiftUI  
**Kind**: method

Dismisses the window defined by the window group that is presenting the specified value type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable
```

#### Discussion

If multiple windows match the provided value, then they all will be dismissed. For dismissing a specific window in a specific group, use `dismissWindow(id:value:)`.

Don’t call this method directly. SwiftUI calls it when you call the [`dismissWindow`](environmentvalues/dismisswindow.md) action with an identifier and a value:

```swift
dismissWindow(value: message.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#Methods-with-Special-Names) in .

## Parameters

- `value`: The value which is currently presented.

## See Also

- [func callAsFunction()](dismisswindowaction/callasfunction.md)
  Dismisses the current window.
- [func callAsFunction(id: String)](dismisswindowaction/callasfunction(id:).md)
  Dismisses the window that’s associated with the specified identifier.
- [func callAsFunction<D>(id: String, value: D)](dismisswindowaction/callasfunction(id:value:).md)
  Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismisswindowaction/callasfunction(value:))*