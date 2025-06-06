# accessibility(sortPriority:)

**Framework**: DeviceActivity  
**Kind**: method

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Higher numbers are sorted first. The default sort priority is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/accessibility(sortpriority:))*