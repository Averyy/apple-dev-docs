# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) init;
```

## Return Value

An array.

## Discussion

After an immutable array has been initialized in this way, it cannot be modified.

This method is a designated initializer.

## See Also

### Initializing an Array
- [convenience init(array: [Any])](./init%28array%29-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./init%28array,copyitems%29.md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.
### Related Documentation
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated array by placing in it the objects in the argument list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init())*