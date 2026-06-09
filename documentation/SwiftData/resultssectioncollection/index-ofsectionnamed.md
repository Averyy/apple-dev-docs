# index(ofSectionNamed:)

**Framework**: SwiftData  
**Kind**: method

Returns the ordered index of the section with the given name, or `nil` if not found.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func index(ofSectionNamed name: SectionName) -> Int?
```

#### Discussion

> **Note**: O(1)

## See Also

- [var sectionNames: [SectionName]](resultssectioncollection/sectionnames.md)
  The section names in order.
- [func contains(sectionName: SectionName) -> Bool](resultssectioncollection/contains(sectionname:).md)
  Returns whether a section with the given name exists in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssectioncollection/index(ofsectionnamed:))*