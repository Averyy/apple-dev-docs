# init(array:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array by placing in it the objects contained in a given array.

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
convenience init(array: [Any])
```

#### Return Value

An array initialized to contain the objects in `anArray`. The returned object might be different than the original receiver.

#### Discussion

After an immutable array has been initialized in this way, it cannot be modified.

## Parameters

- `array`: An array.

## See Also

- [convenience init(object: Any)](nsarray/init(object:).md)
  Creates and returns an array containing a given object.
- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(array:)-o72h)*