# textContentManager(_:textElementAt:)

**Framework**: AppKit  
**Kind**: method

The method the framework calls to return the text element at a specific location.

**Availability**:
- macOS 12.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanagerdelegate/textcontentmanager(_:textelementat:))*