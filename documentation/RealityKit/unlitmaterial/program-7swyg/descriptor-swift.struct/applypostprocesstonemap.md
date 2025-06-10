# applyPostProcessToneMap

**Framework**: RealityKit  
**Kind**: property

A Boolean value that determines whether RealityKit will tonemap the output of this material.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var applyPostProcessToneMap: Bool
```

#### Discussion

If true, the created `UnlitMaterial.Program` will tonemap its color output to better match the rest of the scene; if false, the created `UnlitMaterial.Program` will output its color without modification.

Default value is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/program-7swyg/descriptor-swift.struct/applypostprocesstonemap)*