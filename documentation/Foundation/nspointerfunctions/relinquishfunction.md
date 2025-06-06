# relinquishFunction

**Framework**: Foundation  
**Kind**: property

The function used to relinquish memory.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var relinquishFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Void)? { get set }
```

#### Discussion

This specifies the function to use when an item is removed from a table or pointer array.

## See Also

- [var acquireFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?, ObjCBool) -> UnsafeMutableRawPointer)?](nspointerfunctions/acquirefunction.md)
  The function used to acquire memory.
- [var usesStrongWriteBarrier: Bool](nspointerfunctions/usesstrongwritebarrier.md)
  Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier.
- [var usesWeakReadAndWriteBarriers: Bool](nspointerfunctions/usesweakreadandwritebarriers.md)
  Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/relinquishfunction)*