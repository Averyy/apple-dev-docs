# usesStrongWriteBarrier

**Framework**: Foundation  
**Kind**: property

Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var usesStrongWriteBarrier: Bool { get set }
```

#### Discussion

If you use garbage collection, read and write barrier functions must be used when pointers are from memory scanned by the collector.

## See Also

- [var acquireFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?, ObjCBool) -> UnsafeMutableRawPointer)?](nspointerfunctions/acquirefunction.md)
  The function used to acquire memory.
- [var relinquishFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Void)?](nspointerfunctions/relinquishfunction.md)
  The function used to relinquish memory.
- [var usesWeakReadAndWriteBarriers: Bool](nspointerfunctions/usesweakreadandwritebarriers.md)
  Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/usesstrongwritebarrier)*