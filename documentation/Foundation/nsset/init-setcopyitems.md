# init(set:copyItems:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized set that contains the members of `set`. The returned set might be different than the original receiver.

#### Discussion

After an immutable s has been initialized in this way, it cannot be modified.

The [`copy(with:)`](nscopying/copy(with:).md) method performs a shallow copy. If you have a collection of arbitrary depth, passing [`true`](https://developer.apple.com/documentation/swift/true) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [`false`](https://developer.apple.com/documentation/swift/false) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## Parameters

- `set`: A set containing objects to add to the new set.
- `flag`: If  , then in a managed memory environment each object in   simply receives a   message when it is added to the returned set.

## See Also

- [convenience init(array: [Any])](nsset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsset/init(objects:count:)-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](nsset/init(set:)-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [init()](nsset/init.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(set:copyitems:))*