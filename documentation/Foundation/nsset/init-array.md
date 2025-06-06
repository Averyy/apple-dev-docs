# init(array:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated set with the objects that are contained in a given array.

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
convenience init(array: [Any])
```

#### Return Value

An initialized set with the contents of `array`. The returned set might be different than the original receiver.

## Parameters

- `array`: An array of objects to add to the new set. If the same object appears more than once in  , it is represented only once in the returned set. Each object receives a   message as it is added to the set.

## See Also

- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsset/init(objects:count:)-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](nsset/init(set:)-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](nsset/init(set:copyitems:).md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](nsset/init.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset/init(array:))*