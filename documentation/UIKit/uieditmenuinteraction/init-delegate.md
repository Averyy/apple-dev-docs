# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Initializes an edit menu interaction object with the delegate object you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(delegate: (any UIEditMenuInteractionDelegate)?)
```

#### Discussion

Create an object that conforms to the [`UIEditMenuInteractionDelegate`](uieditmenuinteractiondelegate.md) protocol and assign it to this property. The interaction uses the system delegate if no delegate is provided (if you pass in `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/init(delegate:))*