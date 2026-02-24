# init(array:copyItems:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array using `anArray` as the source of data objects for the array.

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
convenience init(array: [Any], copyItems flag: Bool)
```

#### Return Value

An array initialized to contain the objects—or if `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), copies of the objects—in `array`. The returned object might be different than the original receiver.

#### Discussion

After an immutable array has been initialized in this way, it cannot be modified.

The [`copy(with:)`](nscopying/copy(with:).md) method performs a shallow copy. If you have a collection of arbitrary depth, passing [`true`](https://developer.apple.com/documentation/Swift/true) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [`false`](https://developer.apple.com/documentation/Swift/false) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## Parameters

- `array`: An array containing the objects with which to initialize the new array.
- `flag`: If [`true`](https://developer.apple.com/documentation/Swift/true), each object in `array` receives a [`copyWithZone:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/copyWithZone:) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned array. If [`false`](https://developer.apple.com/documentation/Swift/false), then in a managed memory environment each object in `array` simply receives a `retain` message when it is added to the returned array.

## See Also

- [convenience init(object: Any)](nsarray/init(object:).md)
  Creates and returns an array containing a given object.
- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(array:copyitems:))*