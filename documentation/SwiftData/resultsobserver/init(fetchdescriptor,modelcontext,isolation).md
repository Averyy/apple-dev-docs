# init(fetchDescriptor:modelContext:isolation:)

**Framework**: SwiftData  
**Kind**: init  
**Role**: Initializer

Creates a new unsectioned observer with the given fetch descriptor and model context.

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
convenience init(fetchDescriptor: FetchDescriptor<Element> = FetchDescriptor<Element>(), modelContext: ModelContext, isolation: isolated (any Actor)? = #isolation) throws
```

Available when `Element` conforms to `PersistentModel` and `SectionTitle` is `Never`.

#### Discussion

> **Throws**: An error if the initial fetch fails.

## Parameters

- `fetchDescriptor`: The descriptor defining the fetch criteria.
- `modelContext`: The model context to fetch from and observe for changes.

## See Also

### Creating a results observer with a fetch descriptor
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](./init%28fetchdescriptor,sectionby,modelcontext,isolation%29-7ms14.md)
  Creates a new observer with the given fetch descriptor, a String section key path, and a model context.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String?>, modelContext: ModelContext, isolation: isolated (any Actor)?) throws](./init%28fetchdescriptor,sectionby,modelcontext,isolation%29-9kg1q.md)
  Creates a new observer with the given fetch descriptor, an optional String section key path, and a model context.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](./init%28fetchdescriptor,modelcontainer,isolation%29.md)
  Creates a new unsectioned observer with the given fetch descriptor and model container.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String?>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](./init%28fetchdescriptor,sectionby,modelcontainer,isolation%29-4tuzk.md)
  Creates a new observer with the given fetch descriptor, an optional String section key path, and a model container.
- [convenience init(fetchDescriptor: FetchDescriptor<Element>, sectionBy: KeyPath<Element, String>, modelContainer: ModelContainer, isolation: isolated (any Actor)?) throws](./init%28fetchdescriptor,sectionby,modelcontainer,isolation%29-7wa5c.md)
  Creates a new observer with the given fetch descriptor, a String section key path, and a model container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/init(fetchdescriptor:modelcontext:isolation:))*