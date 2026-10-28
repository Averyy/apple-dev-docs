# accessibilityIdentifier(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Uses the string you specify to identify the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityIdentifier(_ identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Use this value for testing. It isn’t visible to the user.

## See Also

### Identifying elements
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityidentifier(_:))*