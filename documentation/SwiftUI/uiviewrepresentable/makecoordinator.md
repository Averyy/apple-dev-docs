# makeCoordinator()

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the custom instance that you use to communicate changes from your view to other parts of your SwiftUI interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator() -> Self.Coordinator
```

#### Discussion

Implement this method if changes to your view might affect other parts of your app. In your implementation, create a custom Swift instance that can communicate with other parts of your interface. For example, you might provide an instance that binds its variables to SwiftUI properties, causing the two to remain synchronized. If your view doesn’t interact with other parts of your app, providing a coordinator is unnecessary.

SwiftUI calls this method before calling the [`makeUIView(context:)`](uiviewrepresentable/makeuiview(context:).md) method. The system provides your coordinator either directly or as part of a context structure when calling the other methods of your representable instance.

## See Also

- [associatedtype Coordinator = Void](uiviewrepresentable/coordinator.md)
  A type to coordinate with the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/makecoordinator())*