# NSIntegerMapKeyCallBacks

**Framework**: Foundation  
**Kind**: var

For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

**Availability**:
- macOS 10.5+

## Declaration

```swift
let NSIntegerMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

- [let NSIntMapKeyCallBacks: NSMapTableKeyCallBacks](nsintmapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointermapkeycallbacks.md)
  For keys that are pointers not freed.
- [let NSNonOwnedPointerOrNullMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md)
  For keys that are pointers not freed, or `NULL`.
- [let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsobjectmapkeycallbacks.md)
  For keys that are objects.
- [let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsownedpointermapkeycallbacks.md)
  For keys that are pointers, with transfer of ownership upon insertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsintegermapkeycallbacks)*