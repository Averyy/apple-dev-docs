# NSIntegerHashCallBacks

**Framework**: Foundation  
**Kind**: var

For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

**Availability**:
- macOS 10.5+

## Declaration

```swift
let NSIntegerHashCallBacks: NSHashTableCallBacks
```

## See Also

- [let NSNonOwnedPointerHashCallBacks: NSHashTableCallBacks](nsnonownedpointerhashcallbacks.md)
  For sets of pointers, hashed by address.
- [let NSNonRetainedObjectHashCallBacks: NSHashTableCallBacks](nsnonretainedobjecthashcallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectHashCallBacks: NSHashTableCallBacks](nsobjecthashcallbacks.md)
  For sets of objects (similar to `NSSet`).
- [let NSOwnedObjectIdentityHashCallBacks: NSHashTableCallBacks](nsownedobjectidentityhashcallbacks.md)
  For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [let NSOwnedPointerHashCallBacks: NSHashTableCallBacks](nsownedpointerhashcallbacks.md)
  For sets of pointers, with transfer of ownership upon insertion.
- [let NSPointerToStructHashCallBacks: NSHashTableCallBacks](nspointertostructhashcallbacks.md)
  For sets of pointers to structs, when the first field of the struct is `int`-sized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsintegerhashcallbacks)*