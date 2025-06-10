# PhotogrammetrySession.Error.invalidOutput(_:)

**Framework**: RealityKit  
**Kind**: case

An error that represents an invalid output location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
case invalidOutput(URL)
```

#### Discussion

This error occurs in two cases:

1. The URL points to a directory that is not empty.
2. The URL points to a file ending in ‘.usdz’ that already exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/error/invalidoutput(_:))*