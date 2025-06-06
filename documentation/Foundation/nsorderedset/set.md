# set

**Framework**: Foundation  
**Kind**: property

A representation of the set containing the contents of the ordered set.

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
var set: Set<AnyHashable> { get }
```

#### Discussion

This returns a proxy object for the receiving ordered set, which acts like an immutable set.

While you cannot mutate the ordered set through this proxy, mutations to the original ordered set will be reflected in the proxy and it will appear to change spontaneously, because a copy of the ordered set is not being made.

## See Also

- [var array: [Any]](nsorderedset/array.md)
  A representation of the ordered set as an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/set)*