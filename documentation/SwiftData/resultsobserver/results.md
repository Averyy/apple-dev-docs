# results

**Framework**: SwiftData  
**Kind**: property  
**Role**: Instance Property

The current collection of fetched models matching the fetch criteria.

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
final var results: FetchResultsCollection<Element> { get set }
```

## Discussion

This property is updated automatically when relevant changes occur in the model context. As an `@Observable` property, SwiftUI views that read this value will automatically refresh when the results change.

## See Also

### Accessing observer results
- [func element(at: IndexPath) -> Element?](./element%28at%29.md)
  Returns the element at the given index path in the sectioned results.
- [func indexPath(for: Element) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path of the given element within the sectioned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/results)*