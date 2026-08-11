# init(filter:sort:order:animation:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query sorted by a key path, grouped by a required optional-String key path. `nil` values share the empty-string section.

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
@preconcurrency init<Value>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value>, order: SortOrder = .forward, animation: Animation, sectionBy sectionKeyPath: KeyPath<Element, String?>) where Result == SectionedResults<Element, String>, Value : Comparable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:order:animation:sectionby:)-4peqq)*