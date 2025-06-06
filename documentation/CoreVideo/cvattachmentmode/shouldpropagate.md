# CVAttachmentMode.shouldPropagate

**Framework**: Core Video  
**Kind**: case

Indicates to copy the attachment.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case shouldPropagate
```

#### Discussion

The [`CVBufferPropagateAttachments(_:_:)`](cvbufferpropagateattachments(_:_:).md) function propagates all attachments that have this attachment mode. For example, in most cases, you’ll want to propagate an attachment bearing a timestamp to each successive buffer.

## See Also

- [CVAttachmentMode.shouldNotPropagate](cvattachmentmode/shouldnotpropagate.md)
  Indicates to not propagate the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentmode/shouldpropagate)*