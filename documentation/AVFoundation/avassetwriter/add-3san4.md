# add(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds an input group to an asset writer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ inputGroup: AVAssetWriterInputGroup)
```

#### Discussion

An asset writer marks tracks associated with grouped inputs as mutually exclusive to each other for playback or other processing, if the output container format supports mutually exclusive relationships among tracks.

When you add an input group to an asset writer, the system sets the value of the default input’s [`marksOutputTrackAsEnabled`](avassetwriterinput/marksoutputtrackasenabled.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) and sets the values of the group’s other inputs to [`false`](https://developer.apple.com/documentation/Swift/false).

You can’t add input groups after writing starts.

## Parameters

- `inputGroup`: A compatible asset writer input group to add.

## See Also

- [var inputGroups: [AVAssetWriterInputGroup]](avassetwriter/inputgroups.md)
  The input groups an asset writer contains.
- [func canAdd(AVAssetWriterInputGroup) -> Bool](avassetwriter/canadd(_:)-8s1oh.md)
  Determines whether the asset writer supports adding the input group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/add(_:)-3san4)*