# object(at:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the object at the given index path in the fetch results.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func object(at indexPath: IndexPath) -> ResultType
```

```objc
- (ResultType) objectAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

The object at a given index path in the fetch results.

## Parameters

- `indexPath`: An index path in the fetch results.

  If `indexPath` does not describe a valid index path in the fetch results, an exception is raised.

## See Also

### Accessing Results
- [var fetchedObjects: [ResultType]?](./fetchedobjects.md)
  The results of the fetch.
- [func indexPath(forObject: ResultType) -> IndexPath?](./indexpath%28forobject%29.md)
  Returns the index path of a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/object(at:))*