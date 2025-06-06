# object(at:)

**Framework**: Core Data  
**Kind**: method

Returns the object at the given index path in the fetch results.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func object(at indexPath: IndexPath) -> ResultType
```

#### Return Value

The object at a given index path in the fetch results.

## Parameters

- `indexPath`: If   does not describe a valid index path in the fetch results, an exception is raised.

## See Also

- [var fetchedObjects: [ResultType]?](nsfetchedresultscontroller/fetchedobjects.md)
  The results of the fetch.
- [func indexPath(forObject: ResultType) -> IndexPath?](nsfetchedresultscontroller/indexpath(forobject:).md)
  Returns the index path of a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/object(at:))*