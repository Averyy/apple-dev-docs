# resolve(in:)

**Framework**: Foundation Models  
**Kind**: method

Returns the referenced image from the transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func resolve(in transcript: Transcript) -> Transcript.ImageAttachment?
```

#### Return Value

The `ImageAttachment` for this reference, or `nil` if no attachment with label [`attachmentLabel`](imagereference/attachmentlabel.md) is found in the transcript.

## Parameters

- `transcript`: The transcript to resolve the reference against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imagereference/resolve(in:))*