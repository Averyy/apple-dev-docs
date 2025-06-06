# init(predicate:sortBy:)

**Framework**: SwiftData  
**Kind**: init

Creates a fetch descriptor with the specified predicate that, optionally, arranges the fetched models in a particular order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
init(predicate: Predicate<T>? = nil, sortBy: [SortDescriptor<T>] = [])
```

#### Discussion

If you don’t specify a predicate, any fetch using this descriptor will return all models of the associated type. If you expect the number of fetched models to be high, use [`fetchLimit`](fetchdescriptor/fetchlimit.md) and [`fetchOffset`](fetchdescriptor/fetchoffset.md) to break those results into smaller, more efficient batches.

## Parameters

- `predicate`: The logical condition that determines whether the fetch includes a specific model in its results. The default value is  .
- `sortBy`: The array of sort descriptors that tell the fetch how to order its results. The default value is an empty array.

## See Also

- [struct Predicate<each Input>](../Foundation/Predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct SortDescriptor<Compared>](../Foundation/SortDescriptor.md)
  A serializable description of how to sort numerics and strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/init(predicate:sortby:))*