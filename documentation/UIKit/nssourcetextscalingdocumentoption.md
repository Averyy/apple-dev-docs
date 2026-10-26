# NSSourceTextScalingDocumentOption

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The text-scaling mode to associate with the document’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
extern NSAttributedStringDocumentReadingOptionKey const NSSourceTextScalingDocumentOption;
```

#### Discussion

The value of this property is one of the options of the [`NSTextScalingType`](./nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this option to specify the text-scaling mode to associate with the document’s contents on disk.

## See Also

### Getting the font-scaling options
- [NSTargetTextScalingDocumentOption](./nstargettextscalingdocumentoption.md)
  The text scaling mode to use after reading the text from disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nssourcetextscalingdocumentoption)*