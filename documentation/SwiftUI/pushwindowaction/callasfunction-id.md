# callAsFunction(id:)

**Framework**: SwiftUI  
**Kind**: method

Pushes a window that is associated with the specified identifier.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func callAsFunction(id: String)
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`pushWindow`](environmentvalues/pushwindow.md) action with an identifier:

```swift
pushWindow(id: "viewer")
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `id`: The identifier of the scene to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pushwindowaction/callasfunction(id:))*