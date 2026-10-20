# sectionCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The number of sections in the list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var sectionCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger sectionCount;
```

#### Discussion

This value never exceeds [`maximumSectionCount`](./maximumsectioncount.md). If you initialize a list, or call the [`updateSections(_:)`](./updatesections%28_%29.md) method, with an array larger than `maximumSectionCount`, CarPlay trims the array to an appropriate size.

## See Also

### Managing Sections
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sections: [CPListSection]](./sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](./updatesections%28_%29.md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](../cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sectioncount)*