# defaultAttributes

**Framework**: Foundation  
**Kind**: property

The default document attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let defaultAttributes: NSAttributedString.DocumentAttributeKey
```

#### Discussion

The value of this attribute is an [`NSDictionary`](nsdictionary.md) object containing attributes to be applied to plain files. Used by reader methods. This key in options can specify the default attributes applied to the entire document contents. Upon return, the document attributes can contain this key indicating the actual attributes used.

The string constant in macOS 10.3 and earlier is `@"DefaultAttributes"`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/defaultattributes)*