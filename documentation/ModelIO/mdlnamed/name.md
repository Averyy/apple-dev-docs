# name

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

A descriptive name for the object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

Many types of Model I/O objects support this property. For objects loaded from a file using the [`MDLAsset`](mdlasset.md) class, this property may reflect the name or label assigned by an artist using 3D authoring tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlnamed/name)*