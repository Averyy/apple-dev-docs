# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init(time: CMTime, duration: CMTime, direction: FadeCommand.FadeDirection, color: simd_float3, offset: CMTime?)](fadecommand/init(time:duration:direction:color:offset:).md)
  Initializes a color fade command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/init(from:))*