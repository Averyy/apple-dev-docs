# updateSections(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Adds, removes, reorders, or updates the current sections in the list.

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

## Discussion

If the list is visible when you call this method, CarPlay refreshes the list’s appearance to reflect the new items.

## Parameters

- `sections`: The array of sections to display in your list. This initializer copies the array, trimming sections and items as needed to fit within the limits in the [`maximumSectionCount`](./maximumsectioncount.md) and [`maximumItemCount`](./maximumitemcount.md)properties. The initializer trims sections from the end of the array, and keeps adding items section by section until it reaches the maximum.

## See Also

### Managing section content
- [var sectionCount: Int](./sectioncount.md)
  The current number of sections in the list.
- [var sections: [CPListSection]](./sections.md)
  The sections that the list displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/updatesections(_:))*