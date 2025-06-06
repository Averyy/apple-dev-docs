# paste(itemProviders:)

**Framework**: UIKit  
**Kind**: method

Performs a paste operation on the responder object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func paste(itemProviders: [NSItemProvider])
```

#### Discussion

This method performs a paste operation on the responder object, pasting the data provided by specified item providers.

## Parameters

- `itemProviders`: An array of   objects.

## See Also

- [func canPaste([NSItemProvider]) -> Bool](uipasteconfigurationsupporting/canpaste(_:).md)
  Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/paste(itemproviders:))*