# updateUIViewController(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the state of the specified view controller with new information from SwiftUI.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateUIViewController(_ uiViewController: Self.UIViewControllerType, context: Self.Context)
```

#### Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding UIKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## Parameters

- `uiViewController`: Your custom view controller object.
- `context`: A context structure containing information about the current   state of the system.

## See Also

- [func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType](uiviewcontrollerrepresentable/makeuiviewcontroller(context:).md)
  Creates the view controller object and configures its initial state.
- [UIViewControllerRepresentable.Context](uiviewcontrollerrepresentable/context.md)
- [associatedtype UIViewControllerType : UIViewController](uiviewcontrollerrepresentable/uiviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:))*