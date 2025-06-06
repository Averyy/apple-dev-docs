# dsohandle()

**Framework**: Swift  
**Kind**: macro

Produces the dynamic shared object (DSO) handle in use where the macro appears.

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
@freestanding
(expression) macro dsohandle() -> UnsafeRawPointer
```

#### Return Value

The DSO handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dsohandle())*