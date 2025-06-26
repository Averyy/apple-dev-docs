# accessibilityValue(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds a textual description of the value that the view contains.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityValue(_ valueKey: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/accessibilityvalue(_:)-3gvw5)*