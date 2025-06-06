# init(array:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized counted set object with the contents of `array`. The returned object might be different than the original receiver.

## Parameters

- `array`: An array of objects to add to the new set.

## See Also

- [Collections Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [convenience init(array: [Any])](nsset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [convenience init(set: Set<AnyHashable>)](nscountedset/init(set:).md)
  Returns a counted set object initialized with the contents of a given set.
- [init(capacity: Int)](nscountedset/init(capacity:).md)
  Returns a counted set object initialized with enough memory to hold a given number of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/init(array:))*