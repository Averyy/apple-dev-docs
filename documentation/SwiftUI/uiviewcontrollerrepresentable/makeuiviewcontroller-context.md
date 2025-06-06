# makeUIViewController(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the view controller object and configures its initial state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType
```

#### Return Value

Your UIKit view controller configured with the provided information.

#### Discussion

You must implement this method and use it to create your view controller object. Create the view controller using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view controller for the first time. For all subsequent updates, the system calls the [`updateUIViewController(_:context:)`](uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:).md) method.

## Parameters

- `context`: A context structure containing information about   the current state of the system.

## See Also

- [func updateUIViewController(Self.UIViewControllerType, context: Self.Context)](uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:).md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [UIViewControllerRepresentable.Context](uiviewcontrollerrepresentable/context.md)
- [associatedtype UIViewControllerType : UIViewController](uiviewcontrollerrepresentable/uiviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/makeuiviewcontroller(context:))*