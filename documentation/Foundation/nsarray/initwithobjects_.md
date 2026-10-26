# initWithObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a newly allocated array by placing in it the objects in the argument list.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (instancetype) initWithObjects:(ObjectType) firstObj;
```

#### Return Value

An array initialized to include the objects in the argument list. The returned object might be different than the original receiver.

#### Discussion

Pass comma-separated list of trailing variadic arguments as additional objects, ending with `nil`.

After an immutable array has been initialized in this way, it can’t be modified.

This method is a designated initializer.

## Parameters

- `firstObj`: The first object for the array.

## See Also

### Related Documentation
- [+ arrayWithObjects:](./arraywithobjects_.md)
  Creates and returns an array containing the objects in the argument list.
### Initializing an Array
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](./init%28array%29-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./init%28array,copyitems%29.md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/initwithobjects:)*