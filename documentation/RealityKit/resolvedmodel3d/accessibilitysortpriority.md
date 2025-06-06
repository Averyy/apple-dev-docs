# accessibilitySortPriority(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

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
func accessibilitySortPriority(_ sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Higher numbers are sorted first. The default sort priority is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/accessibilitysortpriority(_:))*