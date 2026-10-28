# element(at:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

Returns the element at the given index path in the sectioned results.

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
final func element(at indexPath: IndexPath) -> Element?
```

## Return Value

The element at the given index path, or `nil` if [`sections`](./sections.md) is `nil` or the index path is out of bounds.

## Parameters

- `indexPath`: An index path where `indexPath[0]` is the section index and `indexPath[1]` is the item index within that section.

## See Also

### Accessing observer results
- [var results: FetchResultsCollection<Element>](./results.md)
  The current collection of fetched models matching the fetch criteria.
- [func indexPath(for: Element) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path of the given element within the sectioned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/element(at:))*