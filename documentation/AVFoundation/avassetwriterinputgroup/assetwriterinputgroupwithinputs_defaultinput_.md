# assetWriterInputGroupWithInputs:defaultInput:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new group for the asset writer inputs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetWriterInputGroupWithInputs:(NSArray<AVAssetWriterInput *> *) inputs defaultInput:(AVAssetWriterInput *) defaultInput;
```

#### Return Value

An asset writer input group.

#### Discussion

When you add an input group to an asset writer, the system sets the default input’s [`marksOutputTrackAsEnabled`](../avassetwriterinput/marksoutputtrackasenabled.md) property value to [`true`](../../Swift/true.md), and the value of the other inputs in the group to [`false`](../../Swift/false.md).

## Parameters

- `inputs`: The inputs with tracks to arrange into a mutually exclusive group.
- `defaultInput`: The group’s default input.

## See Also

### Creating an input group
- [init(inputs: [AVAssetWriterInput], defaultInput: AVAssetWriterInput?)](./init%28inputs,defaultinput%29.md)
  Creates a group for the asset writer inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/assetwriterinputgroupwithinputs:defaultinput:)*