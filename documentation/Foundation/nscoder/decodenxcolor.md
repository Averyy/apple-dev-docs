# decodeNXColor

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a color structure from NEXTSTEP Release 3 or earlier.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (NSColor *) decodeNXColor;
```

#### Return Value

An autoreleased `NSColor` object. Returns `nil` if the archived color is invalid.

#### Discussion

This method does not have a matching method for encoding an `NXColor` structure. Encode an `NSColor` object instead.

`NXColor`, a type that dates from pre-OpenStep versions of NEXTSTEP, was a `struct`. Its replacement, `NSColor`, is a class. The difficulties of converting from a `struct` to a class require a special method like [`decodeNXColor`](./decodenxcolor.md).

The [`decodeNXColor`](./decodenxcolor.md) method becomes part of the `NSCoder` class only for apps that use AppKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodenxcolor)*