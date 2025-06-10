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

- [init(commands: [any PresentationCommand])](presentationdescriptor/init(commands:).md)
  Creates an instance containing the commands specified in the array
- [init(duration: CMTime?, commands: [any PresentationCommand])](presentationdescriptor/init(duration:commands:).md)
  Creates an instance containing the commands specified in the array


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptor/init(from:))*