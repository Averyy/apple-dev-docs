# subscript(sectionName:)

**Framework**: SwiftData  
**Kind**: subscript

Returns the section with the given name, or `nil` if no such section exists.

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
subscript(sectionName name: SectionName) -> ResultsSection<Element, SectionName>? { get }
```

#### Overview

> **Note**: O(1)

## See Also

- [struct ResultsSection](resultssection.md)
  A section of fetched results grouped by a common section key path value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultssectioncollection/subscript(sectionname:))*