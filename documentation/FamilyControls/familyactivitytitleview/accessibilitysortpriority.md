# accessibilitySortPriority(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilitySortPriority(_ sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Higher numbers are sorted first. The default sort priority is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/accessibilitysortpriority(_:))*