# init(filter:sort:order:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query sorted by a key path, grouped by a required optional-String key path.

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
@preconcurrency init<Value>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value>, order: SortOrder = .forward, transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String?>) where Result == SectionedResults<Element, String>, Value : Comparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:order:transaction:sectionby:)-68vqy)*