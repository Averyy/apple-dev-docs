# listSectionIndexVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Changes the visibility of the list section index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func listSectionIndexVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

The section index shows the section index labels of sections, which are set using the `sectionIndexLabel` modifier. These are typically the letters of the alphabet, used for sorted sections.

```swift
List(sections) { section in
    Section(section.title) {
        ForEach(section.rows) { row in
            // ...
        }
    }
    .sectionIndexLabel(section.indexTitle)
}
.listSectionIndexVisibility(.visible)
```

On iOS, the section index is displayed as a number of vertically stacked letters on the trailing side of the list. Users can jump to a specific section in the list by tapping on the corresponding index label.

On watchOS, the index of the section currently visible is displayed next to the scroll indicator when the user is scrolling through the list using the crown.

By default, the list section index is visible if the list contains any sections with an index label.

The index only shows labels for sections with a `sectionIndexLabel` modifier. This can be used to hide certain sections from the index.

By hiding section headers of empty sections with an index label, a list section index can be made to show index labels without a corresponding section.

## Parameters

- `visibility`: The visibility of the list section index.

## See Also

- [func sectionIndexLabel(_:)](view/sectionindexlabel(_:).md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionindexvisibility(_:))*