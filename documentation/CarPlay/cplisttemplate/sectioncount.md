# sectionCount

**Framework**: CarPlay  
**Kind**: property

The number of sections in the list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var sectionCount: Int { get }
```

#### Discussion

This value never exceeds [`maximumSectionCount`](cplisttemplate/maximumsectioncount.md). If you initialize a list, or call the [`updateSections(_:)`](cplisttemplate/updatesections(_:).md) method, with an array larger than `maximumSectionCount`, CarPlay trims the array to an appropriate size.

## See Also

- [class var maximumSectionCount: Int](cplisttemplate/maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sections: [CPListSection]](cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](cplisttemplate/updatesections(_:).md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sectioncount)*