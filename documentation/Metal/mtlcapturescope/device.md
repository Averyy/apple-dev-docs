# device

**Framework**: Metal  
**Kind**: property  
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

## See Also

- [var label: String?](mtlcapturescope/label.md)
  A string that helps you identify the capture scope.
- [var commandQueue: (any MTLCommandQueue)?](mtlcapturescope/commandqueue.md)
  The command queue that this capture scope uses to limit which commands are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/device)*