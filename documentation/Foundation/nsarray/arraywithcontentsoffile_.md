# arrayWithContentsOfFile:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an array containing the contents of the file specified by a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```objc
+ (NSArray<id> *) arrayWithContentsOfFile:(NSString *) path;
```

## Return Value

An array containing the contents of the file specified by `aPath`. Returns `nil` if the file can’t be opened or if the contents of the file can’t be parsed into an array.

## Discussion

The array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). For more details, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `path`: The path to a file containing a string representation of an array produced by the [`write(toFile:atomically:)`](./write%28tofile,atomically%29.md) method.

## See Also

### Related Documentation
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the contents of the array to a file at a given path.
### Creating an Array
- [+ array](./array.md)
  Creates and returns an empty array.
- [+ arrayWithArray:](./arraywitharray_.md)
  Creates and returns an array containing the objects in another given array.
- [convenience init(object: Any)](./init%28object%29.md)
  Creates and returns an array containing a given object.
- [+ arrayWithObjects:](./arraywithobjects_.md)
  Creates and returns an array containing the objects in the argument list.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/arraywithcontentsoffile:)*