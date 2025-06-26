# accessibilityHeading(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the accessibility level of this heading.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityHeading(_ level: AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to set the level of this heading in relation to other headings. The system speaks the level number of levels `AccessibilityHeadingLevel/h1` through `AccessibilityHeadingLevel/h6` alongside the text.

The default heading level if you don’t use this modifier is `AccessibilityHeadingLevel/unspecified`.

## Parameters

- `level`: The heading level to associate with this element   from the available   levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/accessibilityheading(_:))*