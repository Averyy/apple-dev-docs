# minLOD

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The lowest mipmap level of detail for the texture.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var minLOD: Float { get }
```

#### Discussion

The property represents the lower limit of the level-of-detail (LOD) range that texture operations access for the texture. When the GPU calculates a mipmap level, it applies the value of this property as the final step, after clamping the sampler LOD and applying the texture view level range offsets.

Each of the following texture operations has a requirement for the `minLOD` value.

| Operation | Requirement |
| --- | --- |
| Read | `floor(minLOD)` ≤ mip level |
| Gather | `floor(minLOD)` ≤ `levelRange.location` |
| Sample | `minLOD` ≤ `levelRange.location` + `levelRange.length` |

Each operation returns an out-of-bounds value if a parameter doesn’t meet a requirement.

> **Note**: For the specific out-of-bounds value for each operation, see the *Texture Functions* section of the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/minlod)*