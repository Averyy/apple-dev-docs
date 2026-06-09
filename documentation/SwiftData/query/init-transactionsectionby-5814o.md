# init(_:transaction:sectionBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a sectioned query from a fetch descriptor, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning.

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
@preconcurrency init(_ descriptor: FetchDescriptor<Element>, transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String?>? = nil) where Result == [Element]
```

## See Also

- [init(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String>?)](query/init(_:animation:sectionby:)-2em2m.md)
  Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path.
- [init(FetchDescriptor<Element>, animation: Animation, sectionBy: KeyPath<Element, String?>?)](query/init(_:animation:sectionby:)-2pqhv.md)
  Creates a sectioned query from a fetch descriptor, grouped by an optional String key path.
- [init(FetchDescriptor<Element>, transaction: Transaction?, sectionBy: KeyPath<Element, String>?)](query/init(_:transaction:sectionby:)-9sb87.md)
  Creates a sectioned query from a fetch descriptor, grouped into sections by a String key path. Pass `nil` to disable sectioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/init(_:transaction:sectionby:)-5814o)*