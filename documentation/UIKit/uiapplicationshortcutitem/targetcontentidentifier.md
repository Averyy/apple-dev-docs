# targetContentIdentifier

**Framework**: UIKit  
**Kind**: property

The object that determines which scene handles the quick action.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var targetContentIdentifier: Any? { get }
```

#### Discussion

UIKit applies the value in this property to the activation conditions defined by the [`UISceneActivationConditions`](uisceneactivationconditions.md) objects of the available scenes. Based on the predicates you specify, UIKit selects the most appropriate scene for handling the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/targetcontentidentifier)*