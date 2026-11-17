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

## Discussion

Specify the sections for your list when creating your list template. To add, remove, reorder, or update the current sections, call the [`updateSections(_:)`](./updatesections%28_%29.md) method.

## See Also

### Managing section content
- [var sectionCount: Int](./sectioncount.md)
  The current number of sections in the list.
- [func updateSections([CPListSection])](./updatesections%28_%29.md)
  Adds, removes, reorders, or updates the current sections in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/sections)*