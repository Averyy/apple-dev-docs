# MTLDispatchType.concurrent

**Framework**: Metal  
**Kind**: case

Sets a command encoder to dispatch encoded commands concurrently during your pass.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case concurrent
```

#### Discussion

If you encode multiple commands that access a single resource, you’re responsible for synchronizing the memory operations to that resource. For more information, see [`Resource synchronization`](resource-synchronization.md).

## See Also

- [MTLDispatchType.serial](mtldispatchtype/serial.md)
  Sets a command encoder to dispatch encoded commands serially during your pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchtype/concurrent)*