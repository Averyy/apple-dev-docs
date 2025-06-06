# level

**Framework**: Metal  
**Kind**: property

The minimum level of messages that the shader can log.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var level: MTLLogLevel { get set }
```

#### Discussion

The default value is [`MTLLogLevel.debug`](mtlloglevel/debug.md).

Use this value to limit which logs from your shader the log state stores. The log state doesn’t store messages at a lower level. Increase the level to reduce verbosity of logging.

## See Also

- [var bufferSize: Int](mtllogstatedescriptor/buffersize.md)
  The size of the internal buffer the log state uses, specified in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogstatedescriptor/level)*