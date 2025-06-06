# NSViewRepresentable

**Framework**: SwiftUI  
**Kind**: protocol

A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency protocol NSViewRepresentable : View where Self.Body == Never
```

#### Overview

Use an `NSViewRepresentable` instance to create and manage an [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object in your SwiftUI interface. Adopt this protocol in one of your app’s custom instances, and use its methods to create, update, and tear down your view. The creation and update processes parallel the behavior of SwiftUI views, and you use them to configure your view with your app’s current state information. Use the teardown process to remove your view cleanly from your SwiftUI. For example, you might use the teardown process to notify other objects that the view is disappearing.

To add your view into your SwiftUI interface, create your [`NSViewRepresentable`](nsviewrepresentable.md) instance and add it to your SwiftUI interface. The system calls the methods of your representable instance at appropriate times to create and update the view. The following example shows the inclusion of a custom `MyRepresentedCustomView` struct in the view hierarchy.

```swift
struct ContentView: View {
   var body: some View {
      VStack {
         Text("Global Sales")
         MyRepresentedCustomView()
      }
   }
}
```

The system doesn’t automatically communicate changes occurring within your view controller to other parts of your SwiftUI interface. When you want your view controller to coordinate with other SwiftUI views, you must provide a [`Coordinator`](nsviewcontrollerrepresentable/coordinator.md) object to facilitate those interactions. For example, you use a coordinator to forward target-action and delegate messages from your view controller to any SwiftUI views.

> ⚠️ **Warning**: SwiftUI fully controls the layout of the AppKit view using the view’s [`frame`](https://developer.apple.com/documentation/AppKit/NSView/frame) and [`bounds`](https://developer.apple.com/documentation/AppKit/NSView/bounds) properties. Don’t directly set these layout-related properties on the view managed by an `NSViewRepresentable` instance from your own code because that conflicts with SwiftUI and results in undefined behavior.

SwiftUI fully controls the layout of the AppKit view using the view’s [`frame`](https://developer.apple.com/documentation/AppKit/NSView/frame) and [`bounds`](https://developer.apple.com/documentation/AppKit/NSView/bounds) properties. Don’t directly set these layout-related properties on the view managed by an `NSViewRepresentable` instance from your own code because that conflicts with SwiftUI and results in undefined behavior.

## Topics

### Creating and updating the view
- [func makeNSView(context: Self.Context) -> Self.NSViewType](nsviewrepresentable/makensview(context:).md)
  Creates the view object and configures its initial state.
- [func updateNSView(Self.NSViewType, context: Self.Context)](nsviewrepresentable/updatensview(_:context:).md)
  Updates the state of the specified view with new information from SwiftUI.
- [NSViewRepresentable.Context](nsviewrepresentable/context.md)
- [associatedtype NSViewType : NSView](nsviewrepresentable/nsviewtype.md)
  The type of view to present.
### Specifying a size
- [func sizeThatFits(ProposedViewSize, nsView: Self.NSViewType, context: Self.Context) -> CGSize?](nsviewrepresentable/sizethatfits(_:nsview:context:).md)
  Given a proposed size, returns the preferred size of the composite view.
### Cleaning up the view
- [static func dismantleNSView(Self.NSViewType, coordinator: Self.Coordinator)](nsviewrepresentable/dismantlensview(_:coordinator:).md)
  Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.
### Providing a custom coordinator object
- [func makeCoordinator() -> Self.Coordinator](nsviewrepresentable/makecoordinator.md)
  Creates the custom instance that you use to communicate changes from your view to other parts of your SwiftUI interface.
- [associatedtype Coordinator = Void](nsviewrepresentable/coordinator.md)
  A type to coordinate with the view.
### Performing layout
- [NSViewRepresentable.LayoutOptions](nsviewrepresentable/layoutoptions.md)

## Relationships

### Inherits From
- [View](view.md)

## See Also

- [struct NSViewRepresentableContext](nsviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view.
- [protocol NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
  A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [struct NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable)*