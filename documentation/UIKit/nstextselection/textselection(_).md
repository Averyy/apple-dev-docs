# textSelection(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a subselection of the current text selection with the ranges you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textSelection(_ textRanges: [NSTextRange]) -> NSTextSelection
```

```objc
- (NSTextSelection *) textSelectionWithTextRanges:(NSArray<NSTextRange *> *) textRanges;
```

#### Return Value

A new [`NSTextSelection`](../nstextselection.md).

## Parameters

- `textRanges`: An array of text ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/textselection(_:))*