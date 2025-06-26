# accessibility(selectionIdentifier:)

**Framework**: FamilyControls  
**Kind**: method

Sets a selection identifier for this view’s accessibility element.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- tvOS 13.0+ - Deprecated
- visionOS 1.0+
- watchOS 6.0+ - Deprecated

## Declaration

```swift
nonisolated
func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Picker uses the value to determine what node to use for the accessibility value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/accessibility(selectionidentifier:))*