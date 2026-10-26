# NSDefaultAttributesDocumentAttribute

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The default document attributes.

**Availability**:
- macOS 10.11+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey NSDefaultAttributesDocumentAttribute;
```

#### Discussion

The value of this attribute is an NSDictionary object containing attributes to be applied to plain files. Used by reader methods. This key in options can specify the default attributes applied to the entire document contents. Upon return, the document attributes can contain this key indicating the actual attributes used.+

The string constant in macOS 10.3 and earlier is `@"DefaultAttributes"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdefaultattributesdocumentattribute)*