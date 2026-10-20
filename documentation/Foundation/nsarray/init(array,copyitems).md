# init(array:copyItems:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithArray:(NSArray<id> *) array copyItems:(BOOL) flag;
```

#### Return Value

An array initialized to contain the objects—or if `flag` is [`true`](../../Swift/true.md), copies of the objects—in `array`. The returned object might be different than the original receiver.

#### Discussion

After an immutable array has been initialized in this way, it cannot be modified.

The [`copy(with:)`](../nscopying/copy%28with%29.md) method performs a shallow copy. If you have a collection of arbitrary depth, passing [`true`](../../Swift/true.md) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [`false`](../../Swift/false.md) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## Parameters

- `array`: An array containing the objects with which to initialize the new array.
- `flag`: If [`true`](../../Swift/true.md), each object in `array` receives a [`copyWithZone:`](../../ObjectiveC/nsobject-swift.class/copywithzone_.md) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned array.

  If [`false`](../../Swift/false.md), then in a managed memory environment each object in `array` simply receives a `retain` message when it is added to the returned array.

## See Also

### Related Documentation
- [convenience init(object: Any)](./init%28object%29.md)
  Creates and returns an array containing a given object.
### Initializing an Array
- [init()](./init%28%29.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](./init%28array%29-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(array:copyitems:))*