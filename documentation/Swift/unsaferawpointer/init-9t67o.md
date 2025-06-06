# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new raw pointer from the given typed pointer.

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
init<T>(_ other: UnsafeMutablePointer<T>) where T : ~Copyable
```

#### Discussion

Use this initializer to explicitly convert `other` to an `UnsafeRawPointer` instance. This initializer creates a new pointer to the same address as `other` and performs no allocation or copying.

## Parameters

- `other`: The typed pointer to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/init(_:)-9t67o)*