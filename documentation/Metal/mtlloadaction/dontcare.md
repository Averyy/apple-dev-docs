# MTLLoadAction.dontCare

**Framework**: Metal  
**Kind**: case

The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case dontCare
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)

## See Also

- [MTLLoadAction.load](mtlloadaction/load.md)
  The GPU preserves the existing contents of the attachment at the start of the render pass.
- [MTLLoadAction.clear](mtlloadaction/clear.md)
  The GPU writes a value to every pixel in the attachment at the start of the render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare)*