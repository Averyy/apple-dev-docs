# storeActionOptions

**Framework**: Metal  
**Kind**: property

The options that modify the store action performed by this attachment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var storeActionOptions: MTLStoreActionOptions { get set }
```

## Mentions

- [Storing Data a Pass Makes with Custom Sample Positions for a Subsequent Pass](storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

#### Discussion

This property specifies additional behavior for the store action specified by the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property.

The default value is [`MTLStoreActionOptionNone`](mtlstoreactionoptions/mtlstoreactionoptionnone.md).

## See Also

- [var loadAction: MTLLoadAction](mtlrenderpassattachmentdescriptor/loadaction.md)
  The action performed by this attachment at the start of a rendering pass for a render command encoder.
- [var storeAction: MTLStoreAction](mtlrenderpassattachmentdescriptor/storeaction.md)
  The action performed by this attachment at the end of a rendering pass for a render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/storeactionoptions)*