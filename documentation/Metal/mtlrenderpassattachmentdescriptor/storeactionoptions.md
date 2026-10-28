# storeActionOptions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The options that modify the store action performed by this attachment.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Store action options have no effect on Apple Silicon

## Declaration

```swift
var storeActionOptions: MTLStoreActionOptions { get set }
```

```objc
@property (nonatomic) MTLStoreActionOptions storeActionOptions;
```

## Mentions

- [Storing data a pass makes with custom sample positions for a subsequent pass](../storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass.md)

## Discussion

This property specifies additional behavior for the store action specified by the [`storeAction`](./storeaction.md) property.

The default value is [`MTLStoreActionOptionNone`](../mtlstoreactionoptions/mtlstoreactionoptionnone.md).

## See Also

### Specifying rendering pass actions
- [var loadAction: MTLLoadAction](./loadaction.md)
  The action performed by this attachment at the start of a rendering pass for a render command encoder.
- [var storeAction: MTLStoreAction](./storeaction.md)
  The action performed by this attachment at the end of a rendering pass for a render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/storeactionoptions)*