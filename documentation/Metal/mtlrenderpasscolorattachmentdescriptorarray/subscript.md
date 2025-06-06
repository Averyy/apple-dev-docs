# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Returns the descriptor object for the specified color attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
subscript(attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor! { get set }
```

#### Return Value

A descriptor object that contains color attachment information.

## Parameters

- `attachmentIndex`: An index in the color attachment array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/subscript(_:))*