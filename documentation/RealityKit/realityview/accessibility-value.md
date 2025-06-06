# accessibility(value:)

**Framework**: RealityKit  
**Kind**: method

Adds a textual description of the value that the view contains.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibility(label:), you can provide the current volume setting, like “60%”, using accessibility(value:).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/accessibility(value:))*