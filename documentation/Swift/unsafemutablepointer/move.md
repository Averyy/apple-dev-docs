# move()

**Framework**: Swift  
**Kind**: method

Retrieves and returns the referenced instance, returning the pointer’s memory to an uninitialized state.

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
func move() -> Pointee
```

#### Return Value

The instance referenced by this pointer.

#### Discussion

Calling the `move()` method on a pointer `p` that references memory of type `T` is equivalent to the following code, aside from any cost and incidental side effects of copying and destroying the value:

```swift
let value: T = {
    defer { p.deinitialize(count: 1) }
    return p.pointee
}()
```

The memory referenced by this pointer must be initialized. After calling `move()`, the memory is uninitialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/move())*