# Query(_:animation:)

**Framework**: SwiftData  
**Kind**: macro

Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@attached
(accessor) @attached(peer, names: prefixed(`_`)) macro Query<Element>(_ descriptor: FetchDescriptor<Element>, animation: Animation) where Element : PersistentModel
```

## Parameters

- `descriptor`: The criteria, sort order, and any additional configuration to use when performing the fetch.
- `animation`: The animation to use when updates to the fetched models trigger user interface changes.

## See Also

- [macro Query<Element>(FetchDescriptor<Element>, transaction: Transaction?)](query(_:transaction:).md)
  Fetches only the subset of the attached model type that satisfy the provided fetch descriptor’s criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query(_:animation:))*