# init(contentsOfFile:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated array with the contents of the file specified by a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
convenience init?(contentsOfFile path: String)
```

```objc
- (NSArray<id> *) initWithContentsOfFile:(NSString *) path;
```

#### Return Value

An array initialized to contain the contents of the file specified by `aPath` or `nil` if the file can’t be opened or the contents of the file can’t be parsed into an array. The returned object might be different than the original receiver.

#### Discussion

The array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `path`: The path to a file containing a representation of an array produced by the [`write(toFile:atomically:)`](./write%28tofile,atomically%29.md) method.

## See Also

### Related Documentation
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the contents of the array to a file at a given path.
### Initializing an Array
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](./init%28array%29-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./init%28array,copyitems%29.md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(contentsoffile:))*