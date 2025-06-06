# indexPath(forObject:)

**Framework**: Core Data  
**Kind**: method

Returns the index path of a given object.

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
func indexPath(forObject object: ResultType) -> IndexPath?
```

#### Return Value

The index path of `object` in the receiver’s fetch results, or `nil` if `object` could not be found.

#### Discussion

In versions of iOS before 3.2, this method raises an exception if `object` is not contained in the receiver’s fetch results.

## Parameters

- `object`: An object in the receiver’s fetch results.

## See Also

- [var fetchedObjects: [ResultType]?](nsfetchedresultscontroller/fetchedobjects.md)
  The results of the fetch.
- [func object(at: IndexPath) -> ResultType](nsfetchedresultscontroller/object(at:).md)
  Returns the object at the given index path in the fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/indexpath(forobject:))*