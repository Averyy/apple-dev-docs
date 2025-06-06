# sectionIndexTitles

**Framework**: Core Data  
**Kind**: property

The array of section index titles.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sectionIndexTitles: [String] { get }
```

#### Discussion

The default implementation returns the array created by calling [`sectionIndexTitle(forSectionName:)`](nsfetchedresultscontroller/sectionindextitle(forsectionname:).md) on all the known sections. You should override this method if you want to return a different array for the section index.

##### Special Considerations

You only need this method if you use a section index.

## See Also

- [func sectionIndexTitle(forSectionName: String) -> String?](nsfetchedresultscontroller/sectionindextitle(forsectionname:).md)
  Returns the corresponding section index entry for a given section name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sectionindextitles)*