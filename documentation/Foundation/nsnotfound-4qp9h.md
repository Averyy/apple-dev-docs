# NSNotFound

**Framework**: Foundation  
**Kind**: var

A value indicating that a requested item couldn’t be found or doesn’t exist.

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
let NSNotFound: Int
```

#### Discussion

`NSNotFound` is typically used by various methods and functions that search for items in serial data and return indices, such as characters in a string object or `id` objects in an `NSArray` object.

##### Special Considerations

Prior to OS X v10.5, `NSNotFound` was defined as `0x7fffffff`. For 32-bit systems, this was effectively the same as `NSIntegerMax`. To support 64-bit environments, `NSNotFound` is now formally defined as `NSIntegerMax`. This means, however, that the value is different in 32-bit and 64-bit environments. You should therefore not save the value directly in files or archives. Moreover, sending the value between 32-bit and 64-bit processes via Distributed Objects will not get you `NSNotFound` on the other side. This applies to any Cocoa methods invoked over Distributed Objects and which might return `NSNotFound`, such as the `indexOfObject:` method of `NSArray` (if sent to a proxy for an array).

## See Also

- [class NSNull](nsnull.md)
  A singleton object used to represent null values in collection objects that don’t allow `nil` values.
- [let NSNotFound: Int](nsnotfound-9t5v2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotfound-4qp9h)*