# init(set:copyItems:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated set and adds to it members of another given set.

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
convenience init(set: Set<AnyHashable>, copyItems flag: Bool)
```

```objc
- (instancetype) initWithSet:(NSSet<id> *) set copyItems:(BOOL) flag;
```

#### Return Value

An initialized set that contains the members of `set`. The returned set might be different than the original receiver.

#### Discussion

After an immutable s has been initialized in this way, it cannot be modified.

The [`copy(with:)`](../nscopying/copy%28with%29.md) method performs a shallow copy. If you have a collection of arbitrary depth, passing [`true`](../../Swift/true.md) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [`false`](../../Swift/false.md) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## Parameters

- `set`: A set containing objects to add to the new set.
- `flag`: If [`true`](../../Swift/true.md), each object in `set` receives a [`copyWithZone:`](../../ObjectiveC/nsobject-swift.class/copywithzone_.md) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned set.

  If [`false`](../../Swift/false.md), then in a managed memory environment each object in `set` simply receives a `retain` message when it is added to the returned set.

## See Also

### Initializing a Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [init()](./init%28%29.md)
  Initializes a newly allocated set.
### Related Documentation
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.
- [+ setWithSet:](./setwithset_.md)
  Creates and returns a set containing the objects from another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(set:copyitems:))*