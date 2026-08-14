# UIAccessibilityCustomAction.Handler

**Framework**: UIKit  
**Kind**: typealias

A closure type that defines a handler to perform for an action.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
typealias Handler = (UIAccessibilityCustomAction) -> Bool
```

## See Also

- [UIAccessibilityAction](../objectivec/uiaccessibilityaction.md)
  A set of methods that accessibility elements can use to support specific actions.
- [class UIAccessibilityCustomAction](uiaccessibilitycustomaction.md)
  A custom action to perform on an accessible object.
- [Delivering an exceptional accessibility experience](../accessibility/delivering_an_exceptional_accessibility_experience.md)
  Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/handler)*