# UIAccessibilityTextAttributeHeadingLevel

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A key for specifying the heading level of the text.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```c
extern NSAttributedStringKey const UIAccessibilityTextAttributeHeadingLevel;
```

#### Overview

The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) object with a value that is a number in the range of `0` to `6`. Use `0` to indicate the absence of a specific heading level, and use other numbers to indicate the heading level.

## See Also

### Constants
- [UIAccessibilityTextAttributeCustom](./uiaccessibilitytextattributecustom.md)
  A key for specifying custom attributes to apply to the text.
- [UIAccessibilityTextAttributeContext](./uiaccessibilitytextattributecontext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitytextattributeheadinglevel)*