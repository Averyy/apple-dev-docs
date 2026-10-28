# textSelection(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a subselection of the current text selection with the ranges you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func textSelection(_ textRanges: [NSTextRange]) -> NSTextSelection
```

```objc
- (NSTextSelection *) textSelectionWithTextRanges:(NSArray<NSTextRange *> *) textRanges;
```

## Return Value

A new [`NSTextSelection`](../nstextselection.md).

## Parameters

- `textRanges`: An array of text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/textselection(_:))*