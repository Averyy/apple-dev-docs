# subelements

**Framework**: App Intents  
**Kind**: property

An array of UI elements that represent subelements in the view hierarchy.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var subelements: [AppEntityUIElement]
```

#### Discussion

This property holds an array of UI elements that represents a UI element’s composition. Each element has no defined coordinate space on its own, but instead uses the coordinate space of the root element. As a result, the bounds of the list of elements a provider returns have the same coordinate space as the provider’s attached view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityuielement/subelements)*