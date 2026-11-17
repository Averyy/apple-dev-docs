# sectionCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current number of sections in the list.

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

## Discussion

This property reflects the total number of sections in the list. The value never exceeds the maximum number of supported sections, as set in the [`maximumSectionCount`](./maximumsectioncount.md) property. If you initialize or update the list with more sections than the allowed maximum, CarPlay discards any sections past the maximum number.

## See Also

### Managing section content
- [var sections: [CPListSection]](./sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](./updatesections%28_%29.md)
  Adds, removes, reorders, or updates the current sections in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sectioncount)*