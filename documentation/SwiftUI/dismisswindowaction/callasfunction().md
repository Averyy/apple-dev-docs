# callAsFunction()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Dismisses the current window.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction()
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`dismissWindow`](../environmentvalues/dismisswindow.md) action:

```swift
dismissWindow()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#Methods-with-Special-Names) in *The Swift Programming Language*.

## See Also

### Calling the action
- [func callAsFunction(id: String)](./callasfunction%28id%29.md)
  Dismisses the window that’s associated with the specified identifier.
- [func callAsFunction<D>(id: String, value: D)](./callasfunction%28id,value%29.md)
  Dismisses the window defined by the window group that is presenting the specified value type and that’s associated with the specified identifier.
- [func callAsFunction<D>(value: D)](./callasfunction%28value%29.md)
  Dismisses the window defined by the window group that is presenting the specified value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismisswindowaction/callasfunction())*