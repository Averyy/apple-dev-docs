# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates a FadeEnvironmentCommand from the specified decoder.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder`: The decoder containing the command to be parsed.

## See Also

- [init(time: CMTime, duration: CMTime, direction: FadeEnvironmentCommand.FadeDirection, opacity: Float, offset: CMTime?)](fadeenvironmentcommand/init(time:duration:direction:opacity:offset:).md)
  Initializes an opacity fade command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand/init(from:))*