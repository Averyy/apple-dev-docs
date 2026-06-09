# results

**Framework**: SwiftData  
**Kind**: property

The current collection of fetched models matching the fetch criteria.

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
final var results: FetchResultsCollection<Element> { get set }
```

#### Discussion

This property is updated automatically when relevant changes occur in the model context. As an `@Observable` property, SwiftUI views that read this value will automatically refresh when the results change.

## See Also

- [func element(at: IndexPath) -> Element?](resultsobserver/element(at:).md)
  Returns the element at the given index path in the sectioned results.
- [func indexPath(for: Element) -> IndexPath?](resultsobserver/indexpath(for:).md)
  Returns the index path of the given element within the sectioned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/results)*