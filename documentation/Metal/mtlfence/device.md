# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device object that created the fence.

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

Only the device that created the fence can use it.

## See Also

- [var label: String?](mtlfence/label.md)
  A string that identifies the fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfence/device)*