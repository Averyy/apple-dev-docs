# init(objects:count:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated set with a specified number of objects from a given C array of objects.

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

```objc
- (instancetype) initWithObjects:(ObjectType const[]) objects count:(NSUInteger) cnt;
```

#### Return Value

An initialized set containing `cnt` objects from the list of objects specified by `objects`. The returned set might be different than the original receiver.

#### Discussion

This method is a designated initializer for `NSSet`.

## Parameters

- `objects`: A C array of objects to add to the new set. If the same object appears more than once in `objects`, it is added only once to the returned set. Each object receives a [`retain`](../../ObjectiveC/nsobject-c.protocol/retain.md) message as it is added to the set.
- `cnt`: The number of objects from `objects` to add to the new set.

## See Also

### Related Documentation
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.
### Initializing a Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](./init%28%29.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(objects:count:)-7kift)*