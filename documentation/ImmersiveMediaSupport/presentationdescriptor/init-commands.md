# init(commands:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an instance containing the commands specified in the array

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(commands: [any PresentationCommand] = [])
```

## Parameters

- `commands`: An array of presentation commands (e.g. SetCameraCommand, FadeCommand)

## See Also

- [init(duration: CMTime?, commands: [any PresentationCommand])](presentationdescriptor/init(duration:commands:).md)
  Creates an instance containing the commands specified in the array
- [init(from: any Decoder) throws](presentationdescriptor/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptor/init(commands:))*