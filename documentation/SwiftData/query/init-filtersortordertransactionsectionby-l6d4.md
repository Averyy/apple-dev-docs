# init(filter:sort:order:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.

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
@preconcurrency init<Value>(filter: Predicate<Element>? = nil, sort keyPath: KeyPath<Element, Value?>, order: SortOrder = .forward, transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String>? = nil) where Result == [Element], Value : Comparable
```

## See Also

- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:animation:sectionby:)-5wk67.md)
  Creates a sectioned query with sort descriptors, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:animation:sectionby:)-8e78r.md)
  Creates a sectioned query with sort descriptors, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-2e9oh.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-2e9oh.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:animation:sectionby:)-4pdmu.md)
  Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:animation:sectionby:)-6b4tq.md)
  Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:animation:sectionby:)-7d51r.md)
  Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:order:transaction:sectionby:)-5ym3e.md)
  Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value?>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:transaction:sectionby:)-8hx6i.md)
  Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init<Value>(filter: Predicate<Element>?, sort: KeyPath<Element, Value>, order: SortOrder, transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:order:transaction:sectionby:)-930wx.md)
  Creates a sectioned query sorted by a key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(filter:sort:transaction:sectionby:)-2b0zd.md)
  Creates a sectioned query with sort descriptors, grouped into sections by a String key path.
- [init(filter: Predicate<Element>?, sort: [SortDescriptor<Element>], transaction: Transaction?, sectionBy: KeyPath<Element, String?>?)](query/init(filter:sort:transaction:sectionby:)-965mg.md)
  Creates a sectioned query with sort descriptors, grouped by an optional String key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:order:transaction:sectionby:)-l6d4)*