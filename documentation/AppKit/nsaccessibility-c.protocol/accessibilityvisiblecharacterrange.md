# accessibilityVisibleCharacterRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The range of visible characters in the document.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property NSRange accessibilityVisibleCharacterRange;
```

## Discussion

Use this property to store the range for entire lines. Characters that are horizontally clipped are included in this range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityvisiblecharacterrange)*