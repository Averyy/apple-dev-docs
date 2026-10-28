# updateUIViewController(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
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

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding UIKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## Parameters

- `uiViewController`: Your custom view controller object.
- `context`: A context structure containing information about the current state of the system.

## See Also

### Creating and updating the view controller
- [func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType](./makeuiviewcontroller%28context%29.md)
  Creates the view controller object and configures its initial state.
- [UIViewControllerRepresentable.Context](./context.md)
- [associatedtype UIViewControllerType : UIViewController](./uiviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/updateuiviewcontroller(_:context:))*