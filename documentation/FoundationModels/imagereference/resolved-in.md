# resolved(in:)

**Framework**: Foundation Models  
**Kind**: method

Returns the referenced image from the transcript.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func resolved(in transcript: some Sequence<Transcript.Entry>) -> Transcript.ImageAttachment?
```

#### Return Value

The [`Transcript.ImageAttachment`](transcript/imageattachment.md) for this reference, or `nil` if no attachment with label [`attachmentLabel`](imagereference/attachmentlabel.md) is found in the transcript.

#### Discussion

If more than one attachment shares an [`attachmentLabel`](imagereference/attachmentlabel.md), the attachment from the latest entry is returned.

## Parameters

- `transcript`: The transcript to resolve the reference against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imagereference/resolved(in:))*