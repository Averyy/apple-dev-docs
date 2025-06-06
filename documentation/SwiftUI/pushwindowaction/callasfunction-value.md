# callAsFunction(value:)

**Framework**: SwiftUI  
**Kind**: method

Pushes a window defined by a window group that presents the type of the specified value.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func callAsFunction<D>(value: D) where D : Decodable, D : Encodable, D : Hashable
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`pushWindow`](environmentvalues/pushwindow.md) action with a value:

```swift
pushWindow(value: video.id)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `value`: The value to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pushwindowaction/callasfunction(value:))*