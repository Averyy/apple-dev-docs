# id

**Framework**: Professional-Video-Applications  
**Role**: Article

Specifies a local identifier to use within the FCPXML document.

#### Overview

Each resource has an `id` attribute that specifies a local identifier to use within the FCPXML document.

For example, the code example below identifies an asset resource with a local identifier of `r1`:

```swift
<asset id="r1" name="MyMovieFile">
   
   <media-rep kind="original-media" src="file:///path/to/MyMovieFile.mov" /> 

</asset>
```

A video or audio element that uses the asset can refer to it by its local identifier in other places in the same FCPXML document.

```swift
<video ref="r1" ... >
```

> **Note**:  Third-party tools may use any string for a local identifier as long as the string begins with a letter and no two resources in the same FCPXML document share the same local identifier.

For most resources, Final Cut Pro also assigns a long unique identifier that it writes when exporting the FCPXML document. Final Cut Pro specifies this unique identifier as a value od the `uid` attribute in the resource.

Except for assets, Final Cut Pro manages unique identifiers, which third-party tools must not generate or alter. For information on asset unique identifier, see [Asset Element Attributes](./asset.md#Asset-Element-Attributes).

Final Cut Pro has both a local identifier and a unique identifier to distinguish between resources that already exist and resources Final Cut Pro imports for the first time. Exported FCPXML documents that refer to existing resources have unique identifiers assigned by Final Cut Pro, whereas imported FCPXML documents that contain new resources only have local identifiers. A local identifier provides an identity for a new resource in an FCPXML document before Final Cut Pro assigns it a permanent unique identifier.

## See Also

### Resource Element Attributes
- [name](./name.md)
  Specifies the name of the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/id)*