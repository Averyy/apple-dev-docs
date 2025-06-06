# init(contentsOfFile:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array with the contents of the file specified by a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(contentsOfFile path: String)
```

#### Return Value

An array initialized to contain the contents of the file specified by `aPath` or `nil` if the file can’t be opened or the contents of the file can’t be parsed into an array. The returned object might be different than the original receiver.

#### Discussion

The array representation in the file identified by `aPath` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `path`: The path to a file containing a representation of an array produced by the   method.

## See Also

- [func write(toFile: String, atomically: Bool) -> Bool](nsarray/write(tofile:atomically:).md)
  Writes the contents of the array to a file at a given path.
- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(contentsoffile:))*