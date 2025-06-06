# CMAttachmentBearer

**Framework**: Core Media  
**Kind**: typealias

An object that can carry attachments.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMAttachmentBearer = CFTypeRef
```

#### Discussion

A `CMAttachmentBearer` is a Core Foundation-based object that supports the suite of key/value/mode attachment APIs. Since “plain” C has no type subclassing, the framework uses `CFType` as the basis for the `CMAttachmentBearer` type. Not all `CFTypes` support `CMAttachmentBearer` methods, so if you call a `CMAttachmentBearer` method on a Core Foundation object that doesn’t support it, it fails.

## See Also

- [protocol CMAttachmentBearerProtocol](cmattachmentbearerprotocol.md)
  A protocol for objects that can carry attachments.
- [typealias CMAttachmentMode](cmattachmentmode.md)
  The mode to use when propagating attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachmentbearer)*