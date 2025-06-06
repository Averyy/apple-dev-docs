# accessibilityTextContentType(_:)

**Framework**: RealityKit  
**Kind**: method

Sets an accessibility text content type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityTextContentType(_ value: AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to set the content type of this accessibility element. Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

The default content type `AccessibilityTextContentType/plain`.

## Parameters

- `value`: The accessibility content type from the available    options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/accessibilitytextcontenttype(_:))*