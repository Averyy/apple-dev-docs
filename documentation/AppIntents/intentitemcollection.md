# IntentItemCollection

**Framework**: App Intents  
**Kind**: struct

Return this object to provide an advanced list of options, optionally divided in sections.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentItemCollection<Result> where Result : _IntentValue
```

#### Example

```swift
struct CreateBookIntent: AppIntent {
    @Parameter(title: "Author Name", optionsProvider: AuthorNamesOptionsProvider())
    var authorName: String

    struct AuthorNamesOptionsProvider: DynamicOptionsProvider {
        func results() async throws -> ItemCollection<Int> {
            ItemCollection {
                ItemSection("Italian Authors") {
                    "Dante Alighieri"
                    "Alessandro Manzoni"
                }
                ItemSection("Russian Authors") {
                    "Anton Chekhov"
                    "Fyodor Dostoevsky"
                }
            }
        }
    }
}
```

## Topics

### Initializers
- [init(promptLabel: LocalizedStringResource?, usesIndexedCollation: Bool, items: [Result])](intentitemcollection/init(promptlabel:usesindexedcollation:items:).md)
  Create a `ItemCollection` containing `Items`, or one or more `Sections`.
- [init(promptLabel: LocalizedStringResource?, usesIndexedCollation: Bool, sections: [IntentItemSection<Result>])](intentitemcollection/init(promptlabel:usesindexedcollation:sections:).md)
  Create an `ItemCollection` containing one or more `Sections`.
- [init(promptLabel: LocalizedStringResource?, usesIndexedCollation: Bool, sectionsBuilder: () -> [IntentItemSection<Result>])](intentitemcollection/init(promptlabel:usesindexedcollation:sectionsbuilder:).md)
  Create an `ItemCollection` containing `Items`, or one or more `Sections` provided by a builder.
### Instance Properties
- [var items: [Result.ValueType]](intentitemcollection/items.md)
  Returns all results as an array.
- [var promptLabel: LocalizedStringResource?](intentitemcollection/promptlabel.md)
  A text prompt shown at the top of the view that presents the options.
- [var sections: [IntentItemSection<Result>]](intentitemcollection/sections.md)
- [var usesIndexedCollation: Bool](intentitemcollection/usesindexedcollation.md)
  If set to true, presents the list of options with an alphabetical index on the right side of the screen (table view section index titles).
### Type Properties
- [static var empty: IntentItemCollection<Result>](intentitemcollection/empty.md)
  Returns an empty result.

## Relationships

### Conforms To
- [ResultsCollection](resultscollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct IntentItem](intentitem.md)
  A type describing a value returned from a dynamic options provider, plus information about how to display it to users.
- [struct IntentItemSection](intentitemsection.md)
  An object you use to divide dynamic options into sections.
- [struct IntentCollectionSize](intentcollectionsize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitemcollection)*