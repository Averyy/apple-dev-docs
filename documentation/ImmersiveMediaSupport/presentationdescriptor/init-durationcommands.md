# init(duration:commands:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an instance containing the commands specified in the array

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(duration: CMTime? = nil, commands: [PresentationCommand] = [])
```

## Parameters

- `duration`: Duration of the metadata commands
- `commands`: An array of presentation commands (e.g. SetCameraCommand, FadeCommand)

## See Also

- [init(commands: [PresentationCommand])](presentationdescriptor/init(commands:).md)
  Creates an instance containing the commands specified in the given array


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptor/init(duration:commands:))*