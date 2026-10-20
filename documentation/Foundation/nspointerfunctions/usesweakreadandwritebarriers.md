# usesWeakReadAndWriteBarriers

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers.

**Availability**:
- iOS 2.0+ - Deprecated in 10.0
- iPadOS 2.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.12
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Garbage collection no longer supported

## Declaration

```swift
var usesWeakReadAndWriteBarriers: Bool { get set }
```

```objc
@property BOOL usesWeakReadAndWriteBarriers;
```

#### Discussion

If you use garbage collection, read and write barrier functions must be used when pointers are from memory scanned by the collector.

## See Also

### Memory Configuration
- [var acquireFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?, ObjCBool) -> UnsafeMutableRawPointer)?](./acquirefunction.md)
  The function used to acquire memory.
- [var relinquishFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Void)?](./relinquishfunction.md)
  The function used to relinquish memory.
- [var usesStrongWriteBarrier: Bool](./usesstrongwritebarrier.md)
  Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/usesweakreadandwritebarriers)*