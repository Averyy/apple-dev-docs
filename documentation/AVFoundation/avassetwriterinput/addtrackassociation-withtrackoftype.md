# addTrackAssociation(withTrackOf:type:)

**Framework**: AVFoundation  
**Kind**: method

Adds an association between input tracks.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String)
```

#### Discussion

The system raises an error if the association type requires tracks of a media type that doesn’t match the input’s type, or if the output file type doesn’t support track associations.

You can’t add track associations after writing starts.

## Parameters

- `input`: The input that contains the track to associate with this input’s track.
- `trackAssociationType`: The type of track association to add.

## See Also

- [func canAddTrackAssociation(withTrackOf: AVAssetWriterInput, type: String) -> Bool](avassetwriterinput/canaddtrackassociation(withtrackof:type:).md)
  Determines whether it’s valid to associate another input’s track with this input’s track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/addtrackassociation(withtrackof:type:))*