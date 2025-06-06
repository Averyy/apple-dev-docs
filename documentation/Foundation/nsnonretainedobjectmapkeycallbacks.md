# NSNonRetainedObjectMapKeyCallBacks

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
let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

- [let NSIntegerMapKeyCallBacks: NSMapTableKeyCallBacks](nsintegermapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSIntMapKeyCallBacks: NSMapTableKeyCallBacks](nsintmapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointermapkeycallbacks.md)
  For keys that are pointers not freed.
- [let NSNonOwnedPointerOrNullMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md)
  For keys that are pointers not freed, or `NULL`.
- [let NSObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsobjectmapkeycallbacks.md)
  For keys that are objects.
- [let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsownedpointermapkeycallbacks.md)
  For keys that are pointers, with transfer of ownership upon insertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnonretainedobjectmapkeycallbacks)*