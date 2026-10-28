# sectionIndexLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the label that is used in a section index to point to this section, typically only a single character long.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@export(implementation)
nonisolated func sectionIndexLabel(_ label: Text?) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func sectionIndexLabel<S>(_ label: S?) -> some View where S : StringProtocol
```

## Discussion

- See also `listSectionIndexVisibility(_:)`

## Parameters

- `label`: The label to display in the section index, or `nil` to display no label for this section.

## See Also

### Configuring a section index
- [func listSectionIndexVisibility(Visibility) -> some View](./listsectionindexvisibility%28_%29.md)
  Changes the visibility of the list section index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sectionindexlabel(_:))*