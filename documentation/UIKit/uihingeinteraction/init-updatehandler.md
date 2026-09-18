# init(updateHandler:)

**Framework**: UIKit  
**Kind**: init

Creates a new hinge interaction with the provided update handler.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
init(updateHandler: @escaping (UIHingeInteraction, UIHingeInteraction.Update) -> Void)
```

#### Discussion

The handler is invoked with the initial hinge state, and again whenever there is an update. An update can occur due to the hinge changing, or when the interaction moves between hierarchies. The handler is stored and escapes, so take care to avoid retain cycles.

## Parameters

- `updateHandler`: Called with the initial hinge state and on each subsequent update for the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihingeinteraction/init(updatehandler:))*