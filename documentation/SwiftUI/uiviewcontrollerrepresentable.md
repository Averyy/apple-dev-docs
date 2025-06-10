# UIViewControllerRepresentable

**Framework**: SwiftUI  
**Kind**: protocol

A view that represents a UIKit view controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol UIViewControllerRepresentable : View where Self.Body == Never
```

#### Overview

Use a [`UIViewControllerRepresentable`](uiviewcontrollerrepresentable.md) instance to create and manage a [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) object in your SwiftUI interface. Adopt this protocol in one of your app’s custom instances, and use its methods to create, update, and tear down your view controller. The creation and update processes parallel the behavior of SwiftUI views, and you use them to configure your view controller with your app’s current state information. Use the teardown process to remove your view controller cleanly from your SwiftUI. For example, you might use the teardown process to notify other objects that the view controller is disappearing.

To add your view controller into your SwiftUI interface, create your [`UIViewControllerRepresentable`](uiviewcontrollerrepresentable.md) instance and add it to your SwiftUI interface. The system calls the methods of your custom instance at appropriate times.

The system doesn’t automatically communicate changes occurring within your view controller to other parts of your SwiftUI interface. When you want your view controller to coordinate with other SwiftUI views, you must provide a [`Coordinator`](nsviewcontrollerrepresentable/coordinator.md) instance to facilitate those interactions. For example, you use a coordinator to forward target-action and delegate messages from your view controller to any SwiftUI views.

> ⚠️ **Warning**: SwiftUI fully controls the layout of the UIKit view controller’s view using the view’s [`center`](https://developer.apple.com/documentation/UIKit/UIView/center), [`bounds`](https://developer.apple.com/documentation/UIKit/UIView/bounds), [`frame`](https://developer.apple.com/documentation/UIKit/UIView/frame), and [`transform`](https://developer.apple.com/documentation/UIKit/UIView/transform) properties. Don’t directly set these layout-related properties on the view managed by a `UIViewControllerRepresentable` instance from your own code because that conflicts with SwiftUI and results in undefined behavior.

## Topics

### Creating and updating the view controller
- [func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType](uiviewcontrollerrepresentable/makeuiviewcontroller(context:).md)
  Creates the view controller object and configures its initial state.
- [func updateUIViewController(Self.UIViewControllerType, context: Self.Context)](uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:).md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [UIViewControllerRepresentable.Context](uiviewcontrollerrepresentable/context.md)
- [associatedtype UIViewControllerType : UIViewController](uiviewcontrollerrepresentable/uiviewcontrollertype.md)
  The type of view controller to present.
### Specifying a size
- [func sizeThatFits(ProposedViewSize, uiViewController: Self.UIViewControllerType, context: Self.Context) -> CGSize?](uiviewcontrollerrepresentable/sizethatfits(_:uiviewcontroller:context:).md)
  Given a proposed size, returns the preferred size of the composite view.
### Cleaning up the view controller
- [static func dismantleUIViewController(Self.UIViewControllerType, coordinator: Self.Coordinator)](uiviewcontrollerrepresentable/dismantleuiviewcontroller(_:coordinator:).md)
  Cleans up the presented view controller (and coordinator) in anticipation of their removal.
### Providing a custom coordinator object
- [func makeCoordinator() -> Self.Coordinator](uiviewcontrollerrepresentable/makecoordinator.md)
  Creates the custom instance that you use to communicate changes from your view controller to other parts of your SwiftUI interface.
- [associatedtype Coordinator = Void](uiviewcontrollerrepresentable/coordinator.md)
  A type to coordinate with the view controller.
### Performing layout
- [UIViewControllerRepresentable.LayoutOptions](uiviewcontrollerrepresentable/layoutoptions.md)

## Relationships

### Inherits From
- [View](view.md)

## See Also

- [protocol UIViewRepresentable](uiviewrepresentable.md)
  A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [struct UIViewRepresentableContext](uiviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view.
- [struct UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable)*