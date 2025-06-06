# init(set:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated set and adds to it objects from another given set.

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
convenience init(set: Set<AnyHashable>)
```

#### Return Value

An initialized objects set containing the objects from `set`. The returned set might be different than the original receiver.

## Parameters

- `set`: A set containing objects to add to the receiving set. Each object is retained as it is added.

## See Also

- [convenience init(array: [Any])](nsset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsset/init(objects:count:)-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](nsset/init(set:copyitems:).md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](nsset/init.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(set:)-1xovx)*