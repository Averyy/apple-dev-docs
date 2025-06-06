# NSOwnedPointerMapKeyCallBacks

**Framework**: Foundation  
**Kind**: var

For keys that are pointers, with transfer of ownership upon insertion.

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
let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks
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
- [let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsobjectmapkeycallbacks.md)
  For keys that are objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsownedpointermapkeycallbacks)*