# body

**Framework**: FinanceKitUI  
**Kind**: property

The content and behavior of the view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/body-swift.property)*