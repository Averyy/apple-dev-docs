# indexPath(for:)

**Framework**: SwiftData  
**Kind**: method  
**Role**: Instance Method

Returns the index path of the given element within the sectioned results.

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
final func indexPath(for element: Element) -> IndexPath?
```

#### Return Value

An index path where `[0]` is the section index and `[1]` is the item index, or `nil` if the object is not found or [`sections`](./sections.md) is `nil`.

## Parameters

- `element`: An element to locate within the sectioned results.

## See Also

### Accessing observer results
- [var results: FetchResultsCollection<Element>](./results.md)
  The current collection of fetched models matching the fetch criteria.
- [func element(at: IndexPath) -> Element?](./element%28at%29.md)
  Returns the element at the given index path in the sectioned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/indexpath(for:))*