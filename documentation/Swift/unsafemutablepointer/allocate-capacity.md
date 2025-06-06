# allocate(capacity:)

**Framework**: Swift  
**Kind**: method

Allocates uninitialized memory for the specified number of instances of type `Pointee`.

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
static func allocate(capacity count: Int) -> UnsafeMutablePointer<Pointee>
```

#### Discussion

The resulting pointer references a region of memory that is bound to `Pointee` and is `count * MemoryLayout<Pointee>.stride` bytes in size.

The following example allocates enough new memory to store four `Int` instances and then initializes that memory with the elements of a range.

```swift
let intPointer = UnsafeMutablePointer<Int>.allocate(capacity: 4)
for i in 0..<4 {
    (intPointer + i).initialize(to: i)
}
print(intPointer.pointee)
// Prints "0"
```

When you allocate memory, always remember to deallocate once you’re finished.

```swift
intPointer.deallocate()
```

## Parameters

- `count`: The amount of memory to allocate, counted in instances   of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/allocate(capacity:))*