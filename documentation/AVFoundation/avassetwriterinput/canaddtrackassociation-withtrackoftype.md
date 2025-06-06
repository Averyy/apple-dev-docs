# canAddTrackAssociation(withTrackOf:type:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether it’s valid to associate another input’s track with this input’s track.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canAddTrackAssociation(withTrackOf input: AVAssetWriterInput, type trackAssociationType: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the system can make the association between tracks; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/swift/false) if the association type requires tracks of a media type that doesn’t match the input’s type, or if the output file type doesn’t support track associations.

## Parameters

- `input`: An asset writer input that contains the track to associate.
- `trackAssociationType`: The type of track association to test.

## See Also

- [func addTrackAssociation(withTrackOf: AVAssetWriterInput, type: String)](avassetwriterinput/addtrackassociation(withtrackof:type:).md)
  Adds an association between input tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/canaddtrackassociation(withtrackof:type:))*