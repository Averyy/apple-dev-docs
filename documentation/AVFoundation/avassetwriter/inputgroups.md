# inputGroups

**Framework**: AVFoundation  
**Kind**: property

The input groups an asset writer contains.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var inputGroups: [AVAssetWriterInputGroup] { get }
```

#### Discussion

Add input groups to the asset writer using its [`add(_:)`](avassetwriter/add(_:)-3san4.md) method.

## See Also

- [func canAdd(AVAssetWriterInputGroup) -> Bool](avassetwriter/canadd(_:)-8s1oh.md)
  Determines whether the asset writer supports adding the input group.
- [func add(AVAssetWriterInputGroup)](avassetwriter/add(_:)-3san4.md)
  Adds an input group to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputgroups)*