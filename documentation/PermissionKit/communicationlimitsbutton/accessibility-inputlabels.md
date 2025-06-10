# accessibility(inputLabels:)

**Framework**: PermissionKit  
**Kind**: method

Sets alternate input labels with which users identify a view.

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
func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the [`accessibility(label:)`](communicationlimitsbutton/accessibility(label:).md) modifier.

## Parameters

- `inputLabels`: An array of Text elements to use as input labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/accessibility(inputlabels:))*