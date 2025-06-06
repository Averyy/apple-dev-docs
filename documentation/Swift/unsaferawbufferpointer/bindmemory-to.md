# bindMemory(to:)

**Framework**: Swift  
**Kind**: method

Binds this buffer’s memory to the specified type and returns a typed buffer of the bound memory.

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
@discardableResult
func bindMemory<T>(to type: T.Type) -> UnsafeBufferPointer<T> where T : ~Copyable
```

#### Return Value

A typed buffer of the newly bound memory. The memory in this region is bound to `T`, but has not been modified in any other way. The typed buffer references `self.count / MemoryLayout<T>.stride` instances of `T`.

#### Discussion

Use the `bindMemory(to:)` method to bind the memory referenced by this buffer to the type `T`. The memory must be uninitialized or initialized to a type that is layout compatible with `T`. If the memory is uninitialized, it is still uninitialized after being bound to `T`.

> ⚠️ **Warning**: A memory location may only be bound to one type at a time. The behavior of accessing memory as a type unrelated to its bound type is undefined.

A memory location may only be bound to one type at a time. The behavior of accessing memory as a type unrelated to its bound type is undefined.

## Parameters

- `type`: The type   to bind the memory to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/bindmemory(to:))*