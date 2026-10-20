# isUniqueReference()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns `true` if `self` holds the only strong reference to its buffer; otherwise, returns `false`.

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
mutating func isUniqueReference() -> Bool
```

#### Discussion

See `isKnownUniquelyReferenced` for details.

## See Also

### Inspecting a Buffer
- [var capacity: Int](./capacity.md)
  The actual number of elements that can be stored in this object.
- [var header: Header](./header.md)
  The stored `Header` instance.
- [var buffer: AnyObject](./buffer.md)
  Returns the object instance being used for storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/isuniquereference())*