# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the capture scope.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Setting this property on a capture scope makes it easier to discover specific capture scopes in Xcode. See `Label Your Capture Scope for Use in the Debug Bar`.

## See Also

- [var device: any MTLDevice](mtlcapturescope/device.md)
  The device object from which you created the capture scope.
- [var commandQueue: (any MTLCommandQueue)?](mtlcapturescope/commandqueue.md)
  The command queue that this capture scope uses to limit which commands are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/label)*