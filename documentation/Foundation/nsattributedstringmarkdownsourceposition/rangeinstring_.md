# rangeInString:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a range indicating the source portion within a Markdown string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```objc
- (NSRange) rangeInString:(NSString *) string;
```

#### Return Value

A range that represents the source portion within a source Markdown string.

#### Discussion

Use this method to access the marked-up region of `string` with an NSRange, rather than making manual calculations based on row and column values.

## Parameters

- `string`: The Markdown source string that this source position object refers to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition/rangeinstring:)*