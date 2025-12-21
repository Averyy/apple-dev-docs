# MTLLoadAction.clear

**Framework**: Metal  
**Kind**: case

The GPU writes a value to every pixel in the attachment at the start of the render pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case clear
```

## Mentions

- [Setting load and store actions](setting-load-and-store-actions.md)

## See Also

- [MTLLoadAction.dontCare](mtlloadaction/dontcare.md)
  The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.
- [MTLLoadAction.load](mtlloadaction/load.md)
  The GPU preserves the existing contents of the attachment at the start of the render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlloadaction/clear)*