# makeArgumentEncoderForBuffer(atIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new argument encoder for a nested argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeArgumentEncoderForBuffer(atIndex index: Int) -> (any MTLArgumentEncoder)?
```

#### Return Value

An argument encoder targeting the nested argument buffer.

#### Discussion

If an argument buffer contains nested argument buffers in its structure, then each nested argument buffer must use its own [`MTLArgumentEncoder`](mtlargumentencoder.md) object to encode its individual resources.

## Parameters

- `index`: The index of a nested argument-buffer within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/makeargumentencoderforbuffer(atindex:))*