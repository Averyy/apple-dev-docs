# init(fetchDescriptor:modelContext:isolation:)

**Framework**: SwiftData  
**Kind**: init

Creates a new unsectioned observer with the given fetch descriptor and model context.

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
convenience init(fetchDescriptor: FetchDescriptor<Element> = FetchDescriptor<Element>(), modelContext: ModelContext, isolation: isolated (any Actor)? = #isolation) throws
```

#### Discussion

> **Note**: An error if the initial fetch fails.

## Parameters

- `fetchDescriptor`: The descriptor defining the fetch criteria.
- `modelContext`: The model context to fetch from and observe for changes.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/init(fetchdescriptor:modelcontext:isolation:))*