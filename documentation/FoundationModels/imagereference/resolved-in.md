# resolved(in:)

**Framework**: Foundation Models  
**Kind**: method

Returns the referenced image from the transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func resolved(in transcript: some Sequence<Transcript.Entry>) -> Transcript.ImageAttachment?
```

#### Return Value

The `ImageAttachment` for this reference, or `nil` if no attachment with label [`attachmentLabel`](imagereference/attachmentlabel.md) is found in the transcript.

#### Discussion

If more than one attachment shares an [`attachmentLabel`](imagereference/attachmentlabel.md), the attachment from the latest entry is returned.

## Parameters

- `transcript`: The transcript to resolve the reference against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/imagereference/resolved(in:))*