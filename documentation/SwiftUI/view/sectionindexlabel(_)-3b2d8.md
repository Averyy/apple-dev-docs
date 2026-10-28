# sectionIndexLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title that is used for the section index label pointing to this section, typically only a single character long.

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
nonisolated func sectionIndexLabel<S>(_ label: S?) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func sectionIndexLabel(_ label: Text?) -> some View
```

## Discussion

- See also `listSectionIndexVisibility(_:)`

## Parameters

- `label`: The title to use for the index label for this section, or `nil` to display no label for this section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sectionindexlabel(_:)-3b2d8)*