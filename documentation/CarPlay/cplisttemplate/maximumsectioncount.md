# maximumSectionCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of sections that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumSectionCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSUInteger maximumSectionCount;
```

## Discussion

This property’s value is dependent on any user interface limits that the vehicle imposes. See [`CPSessionConfiguration`](../cpsessionconfiguration.md) for more information. At runtime, use this value to determine the maximum number of sections that your list can display.

## See Also

### Managing Sections
- [var sectionCount: Int](./sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](./sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](./updatesections%28_%29.md)
  Adds, removes, reorders, or updates the list’s sections.
- [class CPListSection](../cplistsection.md)
  A container that groups your list items into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumsectioncount)*