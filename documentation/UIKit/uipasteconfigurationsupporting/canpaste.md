# canPaste(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func canPaste(_ itemProviders: [NSItemProvider]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the responder object can perform a paste operation using specified item providers; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `itemProviders`: An array of   objects.

## See Also

- [func paste(itemProviders: [NSItemProvider])](uipasteconfigurationsupporting/paste(itemproviders:).md)
  Performs a paste operation on the responder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/canpaste(_:))*