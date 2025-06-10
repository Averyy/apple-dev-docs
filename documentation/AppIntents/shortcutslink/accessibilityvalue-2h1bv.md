# accessibilityValue(_:)

**Framework**: App Intents  
**Kind**: method

Adds a textual description of the value that the view contains.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityValue(_ valueResource: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/accessibilityvalue(_:)-2h1bv)*