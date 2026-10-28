# initWithObjects:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a newly allocated set with members taken from the specified list of objects.

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

## Return Value

An initialized set containing the objects specified in the parameter list. The returned set might be different than the original receiver.

## Discussion

To add additional objects to the new set, pass a comma-separated list of trailing variadic arguments, ending with `nil`.  If the same object appears more than once in the list of objects, it is added only once to the returned set. Each object receives a [`retain`](../../ObjectiveC/nsobject-c.protocol/retain.md) message as it is added to the set.

## Parameters

- `firstObj`: The first object to add to the new set.

## See Also

### Related Documentation
- [+ setWithObjects:](./setwithobjects_.md)
  Creates and returns a set containing the objects in a given argument list.
### Initializing a Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](./init%28%29.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/initwithobjects:)*