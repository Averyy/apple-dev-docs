# mutableCopy(with:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Returns a new instance that’s a mutable copy of the receiver.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 1.0+
- macOS 10.0+
- tvOS 1.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func mutableCopy(with zone: NSZone? = nil) -> Any
```

#### Discussion

The returned object is implicitly retained by the sender, which is responsible for releasing it. The copy returned is mutable whether the original is mutable or not.

## Parameters

- `zone`: This parameter is ignored. Memory zones are no longer used by Objective-C.

## See Also

- [func copy(with: NSZone?) -> Any](nscopying/copy(with:).md)
  Returns a new instance that’s a copy of the receiver.
- [Advanced Memory Management Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)
- [func mutableCopy() -> Any](../ObjectiveC/NSObject-swift.class/mutableCopy.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecopying/mutablecopy(with:))*