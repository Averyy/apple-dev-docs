# init(set:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a counted set object initialized with the contents of a given set.

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

```objc
- (instancetype) initWithSet:(NSSet<id> *) set;
```

#### Return Value

An initialized counted set object with the contents of `set`. The returned object might be different than the original receiver.

## Parameters

- `set`: An set of objects to add to the new set.

## See Also

### Related Documentation
- [convenience init(set: Set<AnyHashable>)](../nsset/init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [+ setWithSet:](../nsset/setwithset_.md)
  Creates and returns a set containing the objects from another set.
### Initializing a Counted Set
- [convenience init(array: [Any])](./init%28array%29.md)
  Returns a counted set object initialized with the contents of a given array.
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns a counted set object initialized with enough memory to hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/init(set:))*