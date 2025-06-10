# sections

**Framework**: CarPlay  
**Kind**: property

The sections that the list displays.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var sections: [CPListSection] { get }
```

#### Discussion

To add new sections to the list, to remove or reorder existing sections, or to update a section’s appearance, use the [`updateSections(_:)`](cplisttemplate/updatesections(_:).md) method.

## See Also

- [class var maximumSectionCount: Int](cplisttemplate/maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](cplisttemplate/sectioncount.md)
  The number of sections in the list.
- [func updateSections([CPListSection])](cplisttemplate/updatesections(_:).md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sections)*