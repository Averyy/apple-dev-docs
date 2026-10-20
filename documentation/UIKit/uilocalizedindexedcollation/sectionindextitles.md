# sectionIndexTitles

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the list of section-index titles for the table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionIndexTitles: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * sectionIndexTitles;
```

#### Discussion

This property contains the localized list of section-index titles sorted according to the specified ordering (for example, A through Z in US English). In its implementation of [`sectionIndexTitles(for:)`](../uitableviewdatasource/sectionindextitles%28for%29.md), the data source can call this method on the indexed-collation object and pass back the result.

## See Also

### Providing section index data to the table view
- [var sectionTitles: [String]](./sectiontitles.md)
  Returns the list of section titles for the table view.
- [func section(forSectionIndexTitle: Int) -> Int](./section%28forsectionindextitle%29.md)
  Returns the section that the table view should scroll to for the given index title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation/sectionindextitles)*