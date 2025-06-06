# sectionIndexTitle(forSectionName:)

**Framework**: Core Data  
**Kind**: method

Returns the corresponding section index entry for a given section name.

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
func sectionIndexTitle(forSectionName sectionName: String) -> String?
```

#### Return Value

The section index entry corresponding to the section with name `sectionName`.

#### Discussion

The default implementation returns the capitalized first letter of the section name.

You should override this method if you need a different way to convert from a section name to its name in the section index.

##### Special Considerations

You only need this method if you use a section index.

## Parameters

- `sectionName`: The name of a section.

## See Also

- [var sectionIndexTitles: [String]](nsfetchedresultscontroller/sectionindextitles.md)
  The array of section index titles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/sectionindextitle(forsectionname:))*