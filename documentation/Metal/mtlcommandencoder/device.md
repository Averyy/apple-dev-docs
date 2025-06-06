# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The Metal device from which the command encoder was created.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

This command encoder can only be used with this [`MTLDevice`](mtldevice.md).

## See Also

- [var label: String?](mtlcommandencoder/label.md)
  A string that labels the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandencoder/device)*