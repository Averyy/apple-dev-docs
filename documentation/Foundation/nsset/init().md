# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated set.

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

#### Return Value

A set.

#### Discussion

This method is a designated initializer of `NSSet`.

## See Also

### Initializing a Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./init%28objects,count%29-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](./init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./init%28set,copyitems%29.md)
  Initializes a newly allocated set and adds to it members of another given set.
- [- initWithObjects:](./initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init())*