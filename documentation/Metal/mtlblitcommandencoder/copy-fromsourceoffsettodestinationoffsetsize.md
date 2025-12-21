# copy(from:sourceOffset:to:destinationOffset:size:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies data from one buffer into another.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func copy(from sourceBuffer: any MTLBuffer, sourceOffset: Int, to destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)
```

## Mentions

- [Copying data to a private resource](copying-data-to-a-private-resource.md)

#### Discussion

You can pass the same buffer to the `sourceBuffer` and `destinationBuffer` parameters if `size` is less than the distance between `sourceOffset` and `destinationOffset`.

> ❗ **Important**:  Copying data to overlapping regions within the same buffer may result in unexpected behavior.

## Parameters

- `sourceBuffer`: A buffer the command copies data from.
- `sourceOffset`: A byte offset within   the command copies from. In macOS,   needs to be a multiple of  , but can be any value in iOS and tvOS.
- `destinationBuffer`: The destination buffer for the copy operation.
- `destinationOffset`: A byte offset within   the command copies to. In macOS,   needs to be a multiple of  , but can be any value in iOS and tvOS.
- `size`: The number of bytes the command copies from   to  . In macOS,   needs to be a multiple of  , but can be any value in iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:))*