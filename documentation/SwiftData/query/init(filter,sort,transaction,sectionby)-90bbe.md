# init(filter:sort:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query with sort descriptors, grouped into sections by a required String key path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency init(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String>) where Result == SectionedResults<Element, String>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:transaction:sectionby:)-90bbe)*