# body

**Framework**: RealityKit  
**Kind**: property

The content and behavior of the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var body: some View { get }
```

#### Discussion

When you implement a custom view, you must implement a computed `body` property to provide the content for your view. Return a view that’s composed of built-in views that SwiftUI provides, plus other composite views that you’ve already defined:

```None
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

For more information about composing views and a view hierarchy, see doc:Declaring-a-Custom-View.

## See Also

- [RealityView.Body](realityview/body-swift.typealias.md)
  The type of view representing the body of this view.
- [RealityView.DefaultPlaceholder](realityview/defaultplaceholder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/body-swift.property)*