# nw_object_t

**Framework**: Network  
**Kind**: typealias

The generic type for objects in the Network framework.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias nw_object_t = any OS_nw_object
```

#### Discussion

Network.framework objects are reference-counted objects that can be used with Automatic Reference Counting (ARC) or directly retained and released.

The objects also conform to the description method of [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) to be used for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_object_t)*