# textElements(for:)

**Framework**: UIKit  
**Kind**: method

Returns an array of text elements that intersect with the range you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textElements(for range: NSTextRange) -> [NSTextElement]
```

#### Return Value

An array of [`NSTextElement`](nstextelement.md).

#### Discussion

This method can return a set of elements that don’t fill the entire range if the entire range isn’t synchronously available. Uses [`enumerateTextElements(from:options:using:)`](nstextelementprovider/enumeratetextelements(from:options:using:).md) to fill the array.

## Parameters

- `range`: An   that describes the range of text to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/textelements(for:))*