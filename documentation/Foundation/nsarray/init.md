# init()

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array.

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
init()
```

#### Return Value

An array.

#### Discussion

After an immutable array has been initialized in this way, it cannot be modified.

This method is a designated initializer.

## See Also

- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init())*