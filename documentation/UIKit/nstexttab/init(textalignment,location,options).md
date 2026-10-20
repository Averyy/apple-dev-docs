# init(textAlignment:location:options:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithTextAlignment:(NSTextAlignment) alignment location:(CGFloat) loc options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An initialized text tab.

#### Discussion

The text alignment is used to determine the position of text inside the tab column. See [`NSParagraphStyle.TextTabType`](../../AppKit/nsparagraphstyle/texttabtype.md) for a mapping between alignments and tab stop types

## Parameters

- `alignment`: The alignment of the text.
- `loc`: The position of the text tab on the ruler, relative to the back margin.
- `options`: Options to apply to the text tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexttab/init(textalignment:location:options:))*