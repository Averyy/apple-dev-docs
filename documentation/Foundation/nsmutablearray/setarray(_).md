# setArray(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiving array’s elements to those in another given array.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setArray(_ otherArray: [Any])
```

```objc
- (void) setArray:(NSArray<id> *) otherArray;
```

## Parameters

- `otherArray`: The array of objects with which to replace the receiving array’s content.

## See Also

### Related Documentation
- [func insert(Any, at: Int)](./insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func addObjects(from: [Any])](./addobjects%28from%29.md)
  Adds the objects contained in another given array to the end of the receiving array’s content.
### Replacing Objects
- [func replaceObject(at: Int, with: Any)](./replaceobject%28at,with%29.md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](./replaceobjects%28at,with%29.md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](./replaceobjects%28in,withobjectsfrom,range%29.md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](./replaceobjects%28in,withobjectsfrom%29.md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/setarray(_:))*