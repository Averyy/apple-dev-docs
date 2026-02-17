# maximumSectionCount

**Framework**: CarPlay  
**Kind**: property

The maximum number of sections that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumSectionCount: Int { get }
```

#### Discussion

This property’s value is dependent on any user interface limits that the vehicle imposes. See [`CPSessionConfiguration`](cpsessionconfiguration.md) for more information. At runtime, use this value to determine the maximum number of sections that your list can display.

## See Also

- [var sectionCount: Int](cplisttemplate/sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](cplisttemplate/updatesections(_:).md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumsectioncount)*