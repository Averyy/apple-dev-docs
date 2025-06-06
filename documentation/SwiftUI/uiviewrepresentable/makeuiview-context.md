# makeUIView(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the view object and configures its initial state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func makeUIView(context: Self.Context) -> Self.UIViewType
```

#### Return Value

Your UIKit view configured with the provided information.

#### Discussion

You must implement this method and use it to create your view object. Configure the view using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view for the first time. For all subsequent updates, the system calls the [`updateUIView(_:context:)`](uiviewrepresentable/updateuiview(_:context:).md) method.

## Parameters

- `context`: A context structure containing information about   the current state of the system.

## See Also

- [func updateUIView(Self.UIViewType, context: Self.Context)](uiviewrepresentable/updateuiview(_:context:).md)
  Updates the state of the specified view with new information from SwiftUI.
- [UIViewRepresentable.Context](uiviewrepresentable/context.md)
- [associatedtype UIViewType : UIView](uiviewrepresentable/uiviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/makeuiview(context:))*