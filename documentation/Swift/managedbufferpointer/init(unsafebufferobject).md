# init(unsafeBufferObject:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Manage the given `buffer`.

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
init(unsafeBufferObject buffer: AnyObject)
```

#### Discussion

> **Precondition**: `buffer` is an instance of a non-`@objc` class whose `deinit` destroys its stored `Header` and any constructed `Element`s.

## See Also

### Creating a Buffer
- [init(bufferClass: AnyClass, minimumCapacity: Int, makingHeaderWith: (AnyObject, (AnyObject) -> Int) throws -> Header) rethrows](./init%28bufferclass,minimumcapacity,makingheaderwith%29.md)
  Create with new storage containing an initial `Header` and space for at least `minimumCapacity` `element`s.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/init(unsafebufferobject:))*