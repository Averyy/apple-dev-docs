# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly, nonnull) id<MTLDevice> device;
```

## Discussion

Only the device that created the fence can use it.

## See Also

### Identifying a fence
- [var label: String?](./label.md)
  A string that identifies the fence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfence/device)*