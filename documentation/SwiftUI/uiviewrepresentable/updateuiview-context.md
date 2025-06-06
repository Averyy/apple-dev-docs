# updateUIView(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the state of the specified view with new information from SwiftUI.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateUIView(_ uiView: Self.UIViewType, context: Self.Context)
```

#### Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding UIKit view. Use this method to update the configuration of your view to match the new state information provided in the `context` parameter.

## Parameters

- `uiView`: Your custom view object.
- `context`: A context structure containing information about the current   state of the system.

## See Also

- [func makeUIView(context: Self.Context) -> Self.UIViewType](uiviewrepresentable/makeuiview(context:).md)
  Creates the view object and configures its initial state.
- [UIViewRepresentable.Context](uiviewrepresentable/context.md)
- [associatedtype UIViewType : UIView](uiviewrepresentable/uiviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/updateuiview(_:context:))*