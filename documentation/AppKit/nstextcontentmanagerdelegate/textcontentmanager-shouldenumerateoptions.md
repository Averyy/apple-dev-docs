# textContentManager(_:shouldEnumerate:options:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the framework should skip this text element in the enumeration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textContentManager(_ textContentManager: NSTextContentManager, shouldEnumerate textElement: NSTextElement, options: NSTextContentManager.EnumerationOptions = []) -> Bool
```

#### Return Value

A Boolean value that informs the framework to skip this `textElement`  in the enumeration. Returning `false` indicates `textElement` to be skipped; otherwise the element is included in the enumeration.

## Parameters

- `textContentManager`: The content manager.
- `textElement`: The   to evaluate.
- `options`: One of the available   options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanagerdelegate/textcontentmanager(_:shouldenumerate:options:))*