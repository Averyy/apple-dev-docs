# textContentManager(_:shouldEnumerate:options:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether the framework should skip this text element in the enumeration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanagerdelegate/textcontentmanager(_:shouldenumerate:options:))*