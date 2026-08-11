# init(filter:sort:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query with sort descriptors, grouped by a required optional-String key path.

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
@MainActor
@preconcurrency init(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String?>) where Result == SectionedResults<Element, String>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:transaction:sectionby:)-353r3)*