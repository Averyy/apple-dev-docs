# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device object that created the argument encoder.

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

#### Discussion

You can only use the encoder to encode data into buffers created by the same Metal device object.

## See Also

- [var label: String?](mtlargumentencoder/label.md)
  A string that identifies the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/device)*