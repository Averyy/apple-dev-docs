# NSSourceTextScalingDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The text-scaling mode you used when creating the text.

**Availability**:
- macOS 10.15+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey const NSSourceTextScalingDocumentAttribute;
```

## Discussion

The value of this property is one of the options of the [`NSTextScalingType`](./nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this attribute to specify the original text-scaling mode you used to create the text.

## See Also

### Getting the font-scaling options
- [NSTextScalingDocumentAttribute](./nstextscalingdocumentattribute.md)
  The text-scaling mode to use when displaying the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssourcetextscalingdocumentattribute)*