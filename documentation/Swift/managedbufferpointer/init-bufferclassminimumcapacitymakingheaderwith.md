# init(bufferClass:minimumCapacity:makingHeaderWith:)

**Framework**: Swift  
**Kind**: init

Create with new storage containing an initial `Header` and space for at least `minimumCapacity` `element`s.

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
init(bufferClass: AnyClass, minimumCapacity: Int, makingHeaderWith factory: (AnyObject, (AnyObject) -> Int) throws -> Header) rethrows
```

#### Discussion

> **Note**: `minimumCapacity >= 0`, and the type indicated by `bufferClass` is a non-`@objc` class with no declared stored properties.  The `deinit` of `bufferClass` must destroy its stored `Header` and any constructed `Element`s.

## Parameters

- `bufferClass`: The class of the object used for storage.
- `minimumCapacity`: The minimum number of  s that   must be able to be stored in the new buffer.
- `factory`: A function that produces the initial    instance stored in the buffer, given the    object and a function that can be called on it to get the actual   number of allocated elements.

## See Also

- [init(unsafeBufferObject: AnyObject)](managedbufferpointer/init(unsafebufferobject:).md)
  Manage the given `buffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/init(bufferclass:minimumcapacity:makingheaderwith:))*