# commandQueue

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The command queue that this capture scope uses to limit which commands are recorded.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var commandQueue: (any MTLCommandQueue)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<MTLCommandQueue> commandQueue;
```

## Discussion

This value is only available if you created the capture scope by calling the [`makeCaptureScope(commandQueue:)`](../mtlcapturemanager/makecapturescope%28commandqueue%29-1rozd.md) method. Otherwise, the value is `nil`.

## See Also

### Identifying the capture scope
- [var label: String?](./label.md)
  A string that helps you identify the capture scope.
- [var device: any MTLDevice](./device.md)
  The device object from which you created the capture scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/commandqueue)*