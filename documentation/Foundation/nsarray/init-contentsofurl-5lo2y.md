# init(contentsOfURL:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array with the contents of the location specified by a given URL.

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
convenience init?(contentsOf url: URL)
```

#### Return Value

An array initialized to contain the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into an array. The returned object might be different than the original receiver.

#### Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `url`: The location of a file containing a string representation of an array produced by the   method.

## See Also

- [init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-fk8x.md)
  Creates and returns an array containing the contents specified by a given URL.
- [func write(to: URL, atomically: Bool) -> Bool](nsarray/write(to:atomically:).md)
  Writes the contents of the array to the location specified by a given URL.
- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(contentsofurl:)-5lo2y)*