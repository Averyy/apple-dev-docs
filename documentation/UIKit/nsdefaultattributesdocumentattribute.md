# NSDefaultAttributesDocumentAttribute

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The default document attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSAttributedStringDocumentAttributeKey const NSDefaultAttributesDocumentAttribute;
```

## Discussion

The value of this attribute is an [`NSDictionary`](../Foundation/nsdictionary.md) object containing attributes to be applied to plain files. Used by reader methods. This key in options can specify the default attributes applied to the entire document contents. Upon return, the document attributes can contain this key indicating the actual attributes used.

The string constant in macOS 10.3 and earlier is `@"DefaultAttributes"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdefaultattributesdocumentattribute)*