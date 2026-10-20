# updateSections(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Adds, removes, reorders, or updates the list’s sections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func updateSections(_ sections: [CPListSection])
```

```objc
- (void) updateSections:(NSArray<CPListSection *> *) sections;
```

#### Discussion

This method is multipurpose. Use it to add new sections to the list, to remove or reorder existing sections, and to update a section’s appearance. At runtime, use [`maximumSectionCount`](./maximumsectioncount.md) to determine the maximum number of sections the list can display. CarPlay trims the array if its size exceeds this limit.

## Parameters

- `sections`: An array of sections to display.

## See Also

### Managing Sections
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](./sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](./sections.md)
  The sections that the list displays.
- [class CPListSection](../cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/updatesections(_:))*