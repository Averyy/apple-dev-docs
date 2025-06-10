# mtl4CommandQueue

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

If set, this scope will only capture Metal commands from the associated Metal 4 command queue. Defaults to nil (all command queues from the associated device are captured).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var mtl4CommandQueue: (any MTL4CommandQueue)? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/mtl4commandqueue)*