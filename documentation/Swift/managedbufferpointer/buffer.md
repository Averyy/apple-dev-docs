# buffer

**Framework**: Swift  
**Kind**: property

Returns the object instance being used for storage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var buffer: AnyObject { get }
```

## See Also

- [var capacity: Int](managedbufferpointer/capacity.md)
  The actual number of elements that can be stored in this object.
- [var header: Header](managedbufferpointer/header.md)
  The stored `Header` instance.
- [func isUniqueReference() -> Bool](managedbufferpointer/isuniquereference.md)
  Returns `true` if `self` holds the only strong reference to its buffer; otherwise, returns `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/buffer)*