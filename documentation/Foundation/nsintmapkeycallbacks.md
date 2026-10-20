# NSIntMapKeyCallBacks

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use `NSIntegerMapKeyCallBacks` instead.

## Declaration

```swift
let NSIntMapKeyCallBacks: NSMapTableKeyCallBacks
```

```c
extern const NSMapTableKeyCallBacks NSIntMapKeyCallBacks;
```

## See Also

### Constants
- [let NSIntegerMapKeyCallBacks: NSMapTableKeyCallBacks](./nsintegermapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](./nsnonownedpointermapkeycallbacks.md)
  For keys that are pointers not freed.
- [let NSNonOwnedPointerOrNullMapKeyCallBacks: NSMapTableKeyCallBacks](./nsnonownedpointerornullmapkeycallbacks.md)
  For keys that are pointers not freed, or `NULL`.
- [let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks](./nsnonretainedobjectmapkeycallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectMapKeyCallBacks: NSMapTableKeyCallBacks](./nsobjectmapkeycallbacks.md)
  For keys that are objects.
- [let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](./nsownedpointermapkeycallbacks.md)
  For keys that are pointers, with transfer of ownership upon insertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsintmapkeycallbacks)*