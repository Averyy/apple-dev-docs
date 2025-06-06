# init(mutating:)

**Framework**: Swift  
**Kind**: init

Creates a new mutable raw pointer from the given immutable raw pointer.

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
init(mutating other: UnsafeRawPointer)
```

#### Discussion

Use this initializer to explicitly convert `other` to an `UnsafeMutableRawPointer` instance. This initializer creates a new pointer to the same address as `other` and performs no allocation or copying.

## Parameters

- `other`: The immutable raw pointer to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawpointer/init(mutating:)-7kfot)*