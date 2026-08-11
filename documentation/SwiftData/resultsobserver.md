# ResultsObserver

**Framework**: SwiftData  
**Kind**: class

Observes and tracks changes to a collection of persistent models in a model context.

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
final class ResultsObserver<Element, SectionTitle> where Element : PersistentModel, SectionTitle : Hashable
```

#### Overview

`ResultsObserver` automatically monitors changes to models that match specified fetch criteria, providing real-time updates when the underlying data changes. The observer maintains a collection of fetched results, making it ideal for keeping user interfaces synchronized with persistent data.

The observer responds to changes from multiple sources:

- Local changes made within the same model context
- Remote changes from other contexts within the same container
- External changes from other processes or CloudKit sync

You can configure the observer using either a complete `FetchDescriptor` or individual filter predicates and sort descriptors. The observer is `Observable`, allowing SwiftUI views to automatically update when results change.

Use `Never` as the `SectionTitle` type parameter when no sectioning is needed:

```swift
let observer = try ResultsObserver<Book, Never>(
    filterBy: #Predicate { $0.isPublished },
    sortBy: [SortDescriptor(\.title)],
    modelContext: context
)
```

Use a concrete type (e.g. `String`) when sectioning by a key path of that type:

```swift
let observer = try ResultsObserver<Book, String>(
    sectionBy: \.genre,
    modelContext: context
)
```

## Topics

### Creating a results observer with a fetch descriptor
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:modelcontext:isolation:).md)
  Creates a new unsectioned observer with the given fetch descriptor and model context.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:sectionby:modelcontext:isolation:)-7ms14.md)
  Creates a new observer with the given fetch descriptor, a String section key path, and a model context.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String?>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:sectionby:modelcontext:isolation:)-9kg1q.md)
  Creates a new observer with the given fetch descriptor, an optional String section key path, and a model context.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:modelcontainer:isolation:).md)
  Creates a new unsectioned observer with the given fetch descriptor and model container.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String?>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:sectionby:modelcontainer:isolation:)-4tuzk.md)
  Creates a new observer with the given fetch descriptor, an optional String section key path, and a model container.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(fetchdescriptor:sectionby:modelcontainer:isolation:)-7wa5c.md)
  Creates a new observer with the given fetch descriptor, a String section key path, and a model container.
### Creating a results observer with a predicate
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:modelcontext:isolation:).md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontext:isolation:)-4ainb.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontext:isolation:)-gsuz.md)
  Creates a new observer with individual filter and sort criteria, a String section key path, and a model context.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:modelcontainer:isolation:).md)
  Creates a new unsectioned observer with individual filter and sort criteria and a model container.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontainer:isolation:)-5ufvn.md)
  Creates a new observer with individual filter and sort criteria, a String section key path, and a model container.
- [convenience init(filterBy: Predicate<Element>?, sortBy: [SortDescriptor<Element>]?, sectionBy: KeyPath<Element, String?>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](resultsobserver/init(filterby:sortby:sectionby:modelcontainer:isolation:)-9lfy0.md)
  Creates a new observer with individual filter and sort criteria, an optional String section key path, and a model container.
### Accessing observer properties
- [var fetchDescriptor: FetchDescriptor<Element>](resultsobserver/fetchdescriptor.md)
  The fetch descriptor used to query the model context.
- [var filterBy: Predicate<Element>?](resultsobserver/filterby.md)
  The predicate used to filter which models are included in the results.
- [let modelContext: ModelContext](resultsobserver/modelcontext.md)
  The model context from which models are fetched.
- [var sortBy: [SortDescriptor<Element>]](resultsobserver/sortby.md)
  The sort descriptors used to order the results.
- [var sectionBy: PartialKeyPath<Element>?](resultsobserver/sectionby.md)
  The key path on the element used to determine section grouping.
- [var sections: SectionedResults<Element, SectionTitle>?](resultsobserver/sections.md)
  The sections computed from the current results, grouped by [`sectionBy`](resultsobserver/sectionby.md).
### Accessing observer results
- [var results: FetchResultsCollection<Element>](resultsobserver/results.md)
  The current collection of fetched models matching the fetch criteria.
- [func element(at: IndexPath) -> Element?](resultsobserver/element(at:).md)
  Returns the element at the given index path in the sectioned results.
- [func indexPath(for: Element) -> IndexPath?](resultsobserver/indexpath(for:).md)
  Returns the index path of the given element within the sectioned results.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Observable](../Observation/Observable.md)

## See Also

- [class HistoryObserver](historyobserver.md)
  Monitors a model container’s data stores for remote changes and notifies when new history transactions are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver)*