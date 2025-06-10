# AttributeScopes.CoreTextAttributes

**Framework**: Foundation  
**Kind**: struct

A namespace for attributes defined by CoreText.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct CoreTextAttributes
```

#### Overview

Note that this is  an [`AttributeScope`](AttributeScope.md), but merely a namespace for [`AttributedStringKey`](AttributedStringKey.md)s that describe CoreText concepts. Those attributes may be used by  to describe those concepts. Unless documented otherwise, frameworks generally inidcate support for a certain attribute by adding it to the framework’s [`AttributeScope`](AttributeScope.md).

CoreText specifically does not support Swift [`AttributedStringKey`](AttributedStringKey.md), and will not recognize the attributes nested in this namespace when used directly with CoreText API, no matter if used in an `AttributedString` or `NSAttributedString`.

## Topics

### Enumerations
- [AttributeScopes.CoreTextAttributes.LineHeightAttribute](attributescopes/coretextattributes/lineheightattribute.md)
  An attribute for defining the height of lines in a text.
- [AttributeScopes.CoreTextAttributes.TextAlignmentAttribute](attributescopes/coretextattributes/textalignmentattribute.md)
  An attribute defining the explicit horizontal alignment of a paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/coretextattributes)*