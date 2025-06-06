# copy(with:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Returns a new instance that’s a copy of the receiver.

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
func copy(with zone: NSZone? = nil) -> Any
```

#### Discussion

The returned object is implicitly retained by the sender, who is responsible for releasing it. The copy returned is immutable if the consideration “immutable vs. mutable” applies to the receiving object; otherwise the exact nature of the copy is determined by the class.

## Parameters

- `zone`: This parameter is ignored. Memory zones are no longer used by Objective-C.

## See Also

- [func mutableCopy(with: NSZone?) -> Any](nsmutablecopying/mutablecopy(with:).md)
  Returns a new instance that’s a mutable copy of the receiver.
- [func copy() -> Any](../ObjectiveC/NSObject-swift.class/copy.md)
  Returns the object returned by `copy(with:)`.
- [Advanced Memory Management Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscopying/copy(with:))*