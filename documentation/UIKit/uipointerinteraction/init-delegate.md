# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Initializes a pointer interaction object with a specified delegate object.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(delegate: (any UIPointerInteractionDelegate)?)
```

#### Discussion

If you create a `UIPointerInteraction` without a delegate by passing `nil` to the initializer, UIKit automatically applies a pointer effect it deems appropriate to the view. Initializing with `nil` is the equivalent of creating a `UIPointerStyle` with [`UIPointerEffect.automatic(_:)`](uipointereffect-swift.enum/automatic(_:).md). Based on the view’s appearance, `.automatic` transforms into one of the concrete effects (`.highlight`, `.lift`, `.hover`).

## Parameters

- `delegate`: An object the framework calls to respond to pointer movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteraction/init(delegate:))*