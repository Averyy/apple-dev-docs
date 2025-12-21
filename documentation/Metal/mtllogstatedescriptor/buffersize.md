# bufferSize

**Framework**: Metal  
**Kind**: property

The size of the internal buffer the log state uses, specified in bytes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var bufferSize: Int { get set }
```

#### Discussion

The default value is 1MB. The minimum size of log buffer is 1KB and the maximum size is 1GB.

Carefully consider the size of this buffer based on how many messages you expect your shader to log and be useful to diagnose problems. A smaller size might lead to the shader dropping more messages while a larger size might result in a larger memory footprint and reduced performance due to excessive logging.

## See Also

- [var level: MTLLogLevel](mtllogstatedescriptor/level.md)
  The minimum level of messages that the shader can log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogstatedescriptor/buffersize)*