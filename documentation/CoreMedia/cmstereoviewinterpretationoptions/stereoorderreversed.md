# stereoOrderReversed

**Framework**: Core Media  
**Kind**: property

Changes the default ordering of eye data, switching it from left-to-right to right-to-left.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var stereoOrderReversed: CMStereoViewInterpretationOptions { get }
```

#### Discussion

Setting the [`stereoOrderReversed`](cmstereoviewinterpretationoptions/stereoorderreversed.md) flag changes interpretations of geometry and affects internal storage.

## See Also

- [static var additionalViews: CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions/additionalviews.md)
  A flag indicating that the video content contains additional views beyond the left or right eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmstereoviewinterpretationoptions/stereoorderreversed)*