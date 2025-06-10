# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an `ImmersiveLensDefinition` object from a ILPD data blob, basically the JSON contents of a ILPD file..

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from data: Data) throws
```

#### Discussion

> **Note**: This function will throw the appropriate error when the data is not well formatted of there are unexpected errors in the JSON.

## See Also

- [init(from: any Decoder) throws](immersivelensdefinition/init(from:)-825gt.md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivelensdefinition/init(from:)-9kmmo)*