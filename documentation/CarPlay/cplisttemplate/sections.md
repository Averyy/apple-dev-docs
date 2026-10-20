# sections

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The sections that the list displays.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sections: [CPListSection] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPListSection *> * sections;
```

#### Discussion

To add new sections to the list, to remove or reorder existing sections, or to update a section’s appearance, use the [`updateSections(_:)`](./updatesections%28_%29.md) method.

## See Also

### Managing Sections
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](./sectioncount.md)
  The number of sections in the list.
- [func updateSections([CPListSection])](./updatesections%28_%29.md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](../cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sections)*