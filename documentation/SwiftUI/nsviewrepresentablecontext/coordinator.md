# coordinator

**Framework**: SwiftUI  
**Kind**: property

An instance you use to communicate your AppKit view’s behavior and state out to SwiftUI objects.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency let coordinator: View.Coordinator
```

#### Discussion

The coordinator is a custom instance you define. When updating your view, communicate changes to SwiftUI by updating the properties of your coordinator, or by calling relevant methods to make those changes. The implementation of those properties and methods are responsible for updating the appropriate SwiftUI values. For example, you might define a property in your coordinator that binds to a SwiftUI value, as shown in the following code example. Changing the property updates the value of the corresponding SwiftUI variable.

```swift
class Coordinator: NSObject {
   @Binding var rating: Int
   init(rating: Binding<Int>) {
      $rating = rating
   }
}
```

To create and configure your custom coordinator, implement the [`makeCoordinator()`](nsviewcontrollerrepresentable/makecoordinator().md) method of your [`NSViewControllerRepresentable`](nsviewcontrollerrepresentable.md) object.

## See Also

- [var transaction: Transaction](nsviewrepresentablecontext/transaction.md)
  The current transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext/coordinator)*