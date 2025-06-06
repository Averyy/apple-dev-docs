# init(objects:count:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array to include a given number of objects from a given C array.

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
init(objects: UnsafePointer<AnyObject>?, count cnt: Int)
```

#### Return Value

A newly allocated array including the first `count` objects from `objects`. The returned object might be different than the original receiver.

#### Discussion

Elements are added to the new array in the same order they appear in `objects`, up to but not including index `count`.

After an immutable array has been initialized in this way, it can’t be modified.

This method is a designated initializer.

## Parameters

- `objects`: A C array of objects.
- `cnt`: The number of values from the   C array to include in the new array. This number will be the count of the new array—it must not be negative or greater than the number of elements in  .

## See Also

- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(objects:count:)-5odxv)*