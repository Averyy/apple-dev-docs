# sectionTitles

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the list of section titles for the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionTitles: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * sectionTitles;
```

## Discussion

This property contains the localized list of section titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [`tableView(_:titleForHeaderInSection:)`](../uitableviewdatasource/tableview%28_,titleforheaderinsection%29.md), the data source can call this method on the indexed-collation object, passing in the section index and returning the result.

## See Also

### Providing section index data to the table view
- [var sectionIndexTitles: [String]](./sectionindextitles.md)
  Returns the list of section-index titles for the table view.
- [func section(forSectionIndexTitle: Int) -> Int](./section%28forsectionindextitle%29.md)
  Returns the section that the table view should scroll to for the given index title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectiontitles)*