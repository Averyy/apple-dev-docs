# NSNonRetainedObjectHashCallBacks

**Framework**: Foundation  
**Kind**: var

For sets of objects, but without retaining/releasing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSNonRetainedObjectHashCallBacks: NSHashTableCallBacks
```

## See Also

- [let NSIntegerHashCallBacks: NSHashTableCallBacks](nsintegerhashcallbacks.md)
  For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerHashCallBacks: NSHashTableCallBacks](nsnonownedpointerhashcallbacks.md)
  For sets of pointers, hashed by address.
- [let NSObjectHashCallBacks: NSHashTableCallBacks](nsobjecthashcallbacks.md)
  For sets of objects (similar to `NSSet`).
- [let NSOwnedObjectIdentityHashCallBacks: NSHashTableCallBacks](nsownedobjectidentityhashcallbacks.md)
  For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [let NSOwnedPointerHashCallBacks: NSHashTableCallBacks](nsownedpointerhashcallbacks.md)
  For sets of pointers, with transfer of ownership upon insertion.
- [let NSPointerToStructHashCallBacks: NSHashTableCallBacks](nspointertostructhashcallbacks.md)
  For sets of pointers to structs, when the first field of the struct is `int`-sized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnonretainedobjecthashcallbacks)*