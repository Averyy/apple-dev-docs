# withBorrowedName(body:)

**Framework**: System  
**Kind**: method

Borrow access to the port name in a block that can perform non-consuming operations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
func withBorrowedName<ReturnType>(body: (mach_port_name_t, mach_port_context_t) -> ReturnType) -> ReturnType
```

#### Discussion

Take care when using this function; many operations consume rights.

If the right is consumed, behavior is undefined.

The body block may optionally return something, which will then be returned to the caller of withBorrowedName.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port/withborrowedname(body:)-8402i)*