# textContentManager(_:textElementAt:)

**Framework**: UIKit  
**Kind**: method

The method the framework calls to return the text element at a specific location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textContentManager(_ textContentManager: NSTextContentManager, textElementAt location: any NSTextLocation) -> NSTextElement?
```

#### Return Value

An [`NSTextElement`](nstextelement.md).

#### Discussion

When non-`nil`, `textContentManager` uses the text element you specify instead of creating one based on its standard mapping logic.

## Parameters

- `textContentManager`: The content manager.
- `location`: The location of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:textelementat:))*