# accessibilityHint(_:)

**Framework**: App Intents  
**Kind**: method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.

> **Note**: On macOS, if the view does not have an action and it has been made into a container with `accessibilityElement(children: .contain)`, this will be used to describe the container. For example, if the container is for a graph, the hint could be “graph”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityhint(_:)-9fgnd)*