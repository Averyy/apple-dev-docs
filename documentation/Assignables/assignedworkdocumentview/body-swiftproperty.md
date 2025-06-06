# body

**Framework**: Assignables  
**Kind**: property

The content and behavior of the view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

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

- [AssignedWorkDocumentView.Document](assignedworkdocumentview/document.md)
  The document type that this view presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/body-swift.property)*