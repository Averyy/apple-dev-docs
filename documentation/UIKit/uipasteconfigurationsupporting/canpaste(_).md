# canPaste(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func canPaste(_ itemProviders: [NSItemProvider]) -> Bool
```

```objc
- (BOOL) canPasteItemProviders:(NSArray<NSItemProvider *> *) itemProviders;
```

## Return Value

[`true`](../../Swift/true.md) if the responder object can perform a paste operation using specified item providers; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `itemProviders`: An array of [`NSItemProvider`](../../Foundation/nsitemprovider.md) objects.

## See Also

### Performing a paste operation
- [func paste(itemProviders: [NSItemProvider])](./paste%28itemproviders%29.md)
  Performs a paste operation on the responder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/canpaste(_:))*