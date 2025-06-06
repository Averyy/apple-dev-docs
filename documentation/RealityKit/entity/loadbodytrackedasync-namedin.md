# loadBodyTrackedAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads a body-tracked entity from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadBodyTrackedAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<BodyTrackedEntity>
```

#### Return Value

A resource loader that publishes the root entity in the loaded file as a [`BodyTrackedEntity`](bodytrackedentity.md).

## Parameters

- `name`: The base name of the file to load, omitting the filename extension.
- `bundle`: The bundle containing the file. Use   to search the app’s   main bundle.

## See Also

- [static func loadBodyTracked(named: String, in: Bundle?) throws -> BodyTrackedEntity](entity/loadbodytracked(named:in:).md)
  Synchronously loads a body-tracked entity from a bundle.
- [static func loadBodyTracked(contentsOf: URL, withName: String?) throws -> BodyTrackedEntity](entity/loadbodytracked(contentsof:withname:).md)
  Synchronously loads a body-tracked entity from a file URL.
- [static func loadBodyTrackedAsync(contentsOf: URL, withName: String?) -> LoadRequest<BodyTrackedEntity>](entity/loadbodytrackedasync(contentsof:withname:).md)
  Asynchronously loads a body-tracked entity from a file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/loadbodytrackedasync(named:in:))*