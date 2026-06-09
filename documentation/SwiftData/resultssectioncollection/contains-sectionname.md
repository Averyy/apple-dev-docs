# contains(sectionName:)

**Framework**: SwiftData  
**Kind**: method

Returns whether a section with the given name exists in the collection.

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
func contains(sectionName name: SectionName) -> Bool
```

#### Discussion

> **Note**: O(1)

## See Also

- [var sectionNames: [SectionName]](resultssectioncollection/sectionnames.md)
  The section names in order.
- [func index(ofSectionNamed: SectionName) -> Int?](resultssectioncollection/index(ofsectionnamed:).md)
  Returns the ordered index of the section with the given name, or `nil` if not found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssectioncollection/contains(sectionname:))*