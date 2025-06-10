# body

**Framework**: App Intents  
**Kind**: property

The content and behavior of the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency var body: some View { get }
```

#### Discussion

When you implement a custom view, you must implement a computed `body` property to provide the content for your view. Return a view that’s composed of built-in views that SwiftUI provides, plus other composite views that you’ve already defined:

```swift
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

For more information about composing views and a view hierarchy, see doc:Declaring-a-Custom-View.

## See Also

- [SiriTipView.Body](siritipview/body-swift.typealias.md)
  The type of view representing the body of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/body-swift.property)*