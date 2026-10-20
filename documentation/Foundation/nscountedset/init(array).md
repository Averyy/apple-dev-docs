# init(array:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a counted set object initialized with the contents of a given array.

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

```objc
- (instancetype) initWithArray:(NSArray<id> *) array;
```

#### Return Value

An initialized counted set object with the contents of `array`. The returned object might be different than the original receiver.

## Parameters

- `array`: An array of objects to add to the new set.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [convenience init(array: [Any])](../nsset/init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
### Initializing a Counted Set
- [convenience init(set: Set<AnyHashable>)](./init%28set%29.md)
  Returns a counted set object initialized with the contents of a given set.
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns a counted set object initialized with enough memory to hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/init(array:))*