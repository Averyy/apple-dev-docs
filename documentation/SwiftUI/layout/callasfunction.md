# callAsFunction(_:)

**Framework**: SwiftUI  
**Kind**: method

Combines the specified views into a single composite view using the layout algorithms of the custom layout container.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func callAsFunction<V>(@ViewBuilder _ content: () -> V) -> some View where V : View
```

#### Return Value

A composite view that combines all the input views.

#### Discussion

Don’t call this method directly. SwiftUI calls it when you instantiate a custom layout that conforms to the [`Layout`](layout.md) protocol:

```swift
BasicVStack { // Implicitly calls callAsFunction.
    Text("A View")
    Text("Another View")
}
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `content`: A   that contains the views to   lay out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/callasfunction(_:))*