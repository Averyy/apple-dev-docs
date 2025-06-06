# MTLVisibilityResultMode.boolean

**Framework**: Metal  
**Kind**: case

The result records whether any samples passed depth and stencil tests.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case boolean
```

#### Discussion

The GPU writes a 64-bit integer to the visibility result buffer that is nonzero if at least one fragment passed depth and stencil tests, and zero if no fragments passed the tests.

## See Also

- [MTLVisibilityResultMode.disabled](mtlvisibilityresultmode/disabled.md)
  The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultMode.counting](mtlvisibilityresultmode/counting.md)
  The result records how many samples passed depth and stencil tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/boolean)*