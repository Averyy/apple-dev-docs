# fromOpaque(_:)

**Framework**: Swift  
**Kind**: method

Unsafely turns an opaque C pointer into an unmanaged class reference.

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
static func fromOpaque(_ value: UnsafeRawPointer) -> Unmanaged<Instance>
```

#### Return Value

An unmanaged class reference to `value`.

#### Discussion

This operation does not change reference counts.

```swift
let str: CFString = Unmanaged.fromOpaque(ptr).takeUnretainedValue()
```

## Parameters

- `value`: An opaque C pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unmanaged/fromopaque(_:))*