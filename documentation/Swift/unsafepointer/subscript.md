# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the pointee at the specified offset from this pointer.

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
subscript(i: Int) -> Pointee { get }
```

#### Overview

For a pointer `p`, the memory at `p + i` must be initialized.

## Parameters

- `i`: The offset from this pointer at which to access an   instance, measured in strides of the pointer’s   type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafepointer/subscript(_:))*