# makeUIView(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
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

## Return Value

Your UIKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object. Configure the view using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view for the first time. For all subsequent updates, the system calls the [`updateUIView(_:context:)`](./updateuiview%28_,context%29.md) method.

## Parameters

- `context`: A context structure containing information about the current state of the system.

## See Also

### Creating and updating the view
- [func updateUIView(Self.UIViewType, context: Self.Context)](./updateuiview%28_,context%29.md)
  Updates the state of the specified view with new information from SwiftUI.
- [UIViewRepresentable.Context](./context.md)
- [associatedtype UIViewType : UIView](./uiviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/makeuiview(context:))*