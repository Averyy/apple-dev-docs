# init(set:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized counted set object with the contents of `set`. The returned object might be different than the original receiver.

## Parameters

- `set`: An set of objects to add to the new set.

## See Also

- [convenience init(set: Set<AnyHashable>)](nsset/init(set:)-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(array: [Any])](nscountedset/init(array:).md)
  Returns a counted set object initialized with the contents of a given array.
- [init(capacity: Int)](nscountedset/init(capacity:).md)
  Returns a counted set object initialized with enough memory to hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/init(set:))*