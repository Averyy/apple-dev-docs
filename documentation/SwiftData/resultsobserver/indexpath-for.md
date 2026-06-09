# indexPath(for:)

**Framework**: SwiftData  
**Kind**: method

Returns the index path of the given element within the sectioned results.

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
final func indexPath(for element: Element) -> IndexPath?
```

#### Return Value

An index path where `[0]` is the section index and `[1]` is the item index, or `nil` if the object is not found or [`sections`](resultsobserver/sections.md) is `nil`.

## Parameters

- `element`: An element to locate within the sectioned results.

## See Also

- [var results: FetchResultsCollection<Element>](resultsobserver/results.md)
  The current collection of fetched models matching the fetch criteria.
- [func element(at: IndexPath) -> Element?](resultsobserver/element(at:).md)
  Returns the element at the given index path in the sectioned results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/resultsobserver/indexpath(for:))*