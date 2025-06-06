# deallocate()

**Framework**: Swift  
**Kind**: method

Deallocates the memory block previously allocated at this pointer.

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
func deallocate()
```

#### Discussion

This pointer must be a pointer to the start of a previously allocated memory block. The memory must not be initialized or `Pointee` must be a trivial type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafepointer/deallocate())*