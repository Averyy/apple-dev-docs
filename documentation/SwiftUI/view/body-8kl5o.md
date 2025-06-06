# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The content and behavior of the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency var body: Self.Body { get }
```

## Mentions

- [Declaring a custom view](declaring-a-custom-view.md)

#### Discussion

When you implement a custom view, you must implement a computed `body` property to provide the content for your view. Return a view that’s composed of built-in views that SwiftUI provides, plus other composite views that you’ve already defined:

```swift
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

For more information about composing views and a view hierarchy, see [`Declaring a custom view`](declaring-a-custom-view.md).

## See Also

- [associatedtype Body : View](view/body-swift.associatedtype.md)
  The type of view representing the body of this view.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](view/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [Previews in Xcode](previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/body-8kl5o)*