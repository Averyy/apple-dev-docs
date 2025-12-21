# canAdd(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether the asset writer supports adding the input group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canAdd(_ inputGroup: AVAssetWriterInputGroup) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you can add the input group to the asset writer; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) if the asset writer’s output file type doesn’t support mutually exclusive relationships among tracks, or if the input group contains inputs with media types that you can’t relate.

## Parameters

- `inputGroup`: The asset writer input group to add.

## See Also

- [var inputGroups: [AVAssetWriterInputGroup]](avassetwriter/inputgroups.md)
  The input groups an asset writer contains.
- [func add(AVAssetWriterInputGroup)](avassetwriter/add(_:)-3san4.md)
  Adds an input group to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/canadd(_:)-8s1oh)*