# NSTargetTextScalingDocumentOption

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The text scaling mode to use after reading the text from disk.

**Availability**:
- macOS 10.15+

## Declaration

```c
extern NSAttributedStringDocumentReadingOptionKey const NSTargetTextScalingDocumentOption;
```

#### Discussion

The value of this property is one of the options of the [`NSTextScalingType`](./nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this option to specify the text-scaling mode you want to use for the document you read.

## See Also

### Getting the font-scaling options
- [NSSourceTextScalingDocumentOption](./nssourcetextscalingdocumentoption.md)
  The text-scaling mode to associate with the document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstargettextscalingdocumentoption)*