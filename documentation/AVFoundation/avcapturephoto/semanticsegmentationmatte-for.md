# semanticSegmentationMatte(for:)

**Framework**: Avfoundation  
**Kind**: method

Retrieves the semantic segmentation matte associated with this photo.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func semanticSegmentationMatte(for semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType) -> AVSemanticSegmentationMatte?
```

#### Return Value

An instance of [`AVSemanticSegmentationMatte`](avsemanticsegmentationmatte.md), or `nil` of you didn’t request semantic segmentation matte delivery or if no mattes of the specified type were found.

#### Discussion

If you requested one or more semantic segmentation mattes by calling [`enabledSemanticSegmentationMatteTypes`](avcapturephotosettings/enabledsemanticsegmentationmattetypes.md) with a nonempty array of types, this property offers access to the resulting [`AVSemanticSegmentationMatte`](avsemanticsegmentationmatte.md) objects.

> **Note**:  Semantic segmentation mattes are only embedded in the photo’s internal file format container if you set [`embedsSemanticSegmentationMattesInPhoto`](avcapturephotosettings/embedssemanticsegmentationmattesinphoto.md) to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `semanticSegmentationMatteType`: The type of semantic segmentation matte to retrieve from the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/semanticsegmentationmatte(for:))*