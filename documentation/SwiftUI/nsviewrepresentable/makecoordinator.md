# makeCoordinator()

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the custom instance that you use to communicate changes from your view to other parts of your SwiftUI interface.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator() -> Self.Coordinator
```

#### Discussion

Implement this method if changes to your view might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view doesn’t interact with other parts of your app, you don’t have to provide a coordinator.

SwiftUI calls this method before calling the [`makeNSView(context:)`](nsviewrepresentable/makensview(context:).md) method. The system provides your coordinator instance either directly or as part of a context structure when calling the other methods of your representable instance.

## See Also

- [associatedtype Coordinator = Void](nsviewrepresentable/coordinator.md)
  A type to coordinate with the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makecoordinator())*