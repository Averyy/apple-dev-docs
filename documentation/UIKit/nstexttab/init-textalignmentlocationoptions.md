# init(textAlignment:location:options:)

**Framework**: UIKit  
**Kind**: init

Initializes a text tab with the specified text alignment, location, and options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options: [NSTextTab.OptionKey : Any] = [:])
```

#### Return Value

An initialized text tab.

#### Discussion

The text alignment is used to determine the position of text inside the tab column. See [`NSParagraphStyle.TextTabType`](https://developer.apple.com/documentation/AppKit/NSParagraphStyle/TextTabType) for a mapping between alignments and tab stop types

## Parameters

- `alignment`: The alignment of the text.
- `loc`: The position of the text tab on the ruler, relative to the back margin.
- `options`: Options to apply to the text tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttab/init(textalignment:location:options:))*