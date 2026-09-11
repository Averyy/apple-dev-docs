# sections

**Framework**: SwiftData  
**Kind**: property

The sections computed from the current results, grouped by the `sectionBy` key path.

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