# init(from:)

**Framework**: Immersive Media Support  
**Kind**: init

Creates an `ImmersiveCameraLensDefinition` object from a ILPD data blob, basically the JSON contents of a ILPD file..

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(from data: Data) throws
```

#### Discussion

> **Note**: This function throws an appropriate error when the data is not well formatted of there are unexpected errors in the JSON.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition/init(from:))*