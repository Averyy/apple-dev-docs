# MTLVisibilityResultMode.counting

**Framework**: Metal  
**Kind**: case

The result records how many samples passed depth and stencil tests.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case counting
```

#### Discussion

The GPU writes a 64-bit integer to the visibility result buffer that is the number of samples that passed depth and stencil tests; this can be zero. Counting is not supported by all GPUs. Check the following documents to see whether a GPU family supports  queries:

- [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [`Metal feature set tables (Numbers)`](https://developer.apple.comhttps://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

- [MTLVisibilityResultMode.disabled](mtlvisibilityresultmode/disabled.md)
  The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultMode.boolean](mtlvisibilityresultmode/boolean.md)
  The result records whether any samples passed depth and stencil tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/counting)*