# init(unsafeBufferObject:)

**Framework**: Swift  
**Kind**: init

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

> **Note**: `buffer` is an instance of a non-`@objc` class whose `deinit` destroys its stored `Header` and any constructed `Element`s.

`buffer` is an instance of a non-`@objc` class whose `deinit` destroys its stored `Header` and any constructed `Element`s.

## See Also

- [init(bufferClass: AnyClass, minimumCapacity: Int, makingHeaderWith: (AnyObject, (AnyObject) -> Int) throws -> Header) rethrows](managedbufferpointer/init(bufferclass:minimumcapacity:makingheaderwith:).md)
  Create with new storage containing an initial `Header` and space for at least `minimumCapacity` `element`s.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/init(unsafebufferobject:))*