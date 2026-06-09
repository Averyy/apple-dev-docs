# sections

**Framework**: SwiftData  
**Kind**: property

The sections computed from the current results, grouped by the `sectionBy` key path.

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
@preconcurrency var sections: ResultsSectionCollection<Element, String> { get }
```

#### Discussion

Section names are `String`-typed. Both `KeyPath<Element, String>` and `KeyPath<Element, String?>` section keys produce `String` names — `nil` values map to the empty-string section.

Returns an empty collection when the query was not created with a `sectionBy` parameter. Access this from the query’s stored property using the underscore prefix:

```swift
struct ItemList: View {
    @Query(sort: \.category, sectionBy: \.category)
    var items: [Item]

    var body: some View {
        List {
            ForEach(_items.sections) { section in
                Section(section.name) {
                    ForEach(section) { item in Text(item.name) }
                }
            }
        }
    }
}
```

## See Also

- [struct ResultsSectionCollection](resultssectioncollection.md)
  A collection of sections as returned by [`sections`](resultsobserver/sections.md) or `Query.sections`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/sections)*