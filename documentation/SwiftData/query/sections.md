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
@preconcurrency var sections: SectionedResults<Element, String> { get }
```

#### Discussion

Section names are `String`-typed. Both `KeyPath<Element, String>` and `KeyPath<Element, String?>` section keys produce `String` names — `nil` values map to the empty-string section.

Returns an empty collection when the query was not created with a `sectionBy` parameter. For `SectionedResults`-typed queries, access sections through the property directly; for `[Element]`-typed queries, use the underscore-prefix accessor:

```swift
// Preferred — SectionedResults result type
@Query(sort: \.name, sectionBy: \.category)
var items: SectionedResults<Item, String>

var body: some View {
    List {
        ForEach(items) { section in
            Section(section.title) {
                ForEach(section) { item in Text(item.name) }
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/sections)*