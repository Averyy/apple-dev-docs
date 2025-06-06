# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device object that created the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

A heap is always associated with the [`MTLDevice`](mtldevice.md) that created it and can be used only with that device.

## See Also

- [var label: String?](mtlheap/label.md)
  A string that identifies the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/device)*