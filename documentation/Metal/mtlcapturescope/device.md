# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The device object from which you created the capture scope.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (nonatomic, readonly, nonnull) id<MTLDevice> device;
```

## See Also

### Identifying the capture scope
- [var label: String?](./label.md)
  A string that helps you identify the capture scope.
- [var commandQueue: (any MTLCommandQueue)?](./commandqueue.md)
  The command queue that this capture scope uses to limit which commands are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/device)*