# kCMTagStereoInterpretationOrderReversed

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

A value for a stereo interpretation tag indicating the video data for the left and right eyes are reversed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern const CMTag kCMTagStereoInterpretationOrderReversed;
```

#### Discussion

This value is for use in tags with the [`kCMTagCategory_StereoViewInterpretation`](./cmtagcategory/kcmtagcategory_stereoviewinterpretation.md) category. This constant changes interpretations of geometry and affects internal storage by placing right eye data before left eye data.

## See Also

### 3D Video Data
- [kCMTagStereoLeftAndRightEye](./kcmtagstereoleftandrighteye.md)
  A value for a stereo tag indicating the video track has left and right eye layers.
- [kCMTagStereoLeftEye](./kcmtagstereolefteye.md)
  A value for a stereo tag indicating the video track has a left eye layer.
- [kCMTagStereoRightEye](./kcmtagstereorighteye.md)
  A value for a stereo tag indicating the video track has a right eye layer.
- [kCMTagStereoNone](./kcmtagstereonone.md)
  A value for a stereo tag indicating the video track has no eye layer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtagstereointerpretationorderreversed)*