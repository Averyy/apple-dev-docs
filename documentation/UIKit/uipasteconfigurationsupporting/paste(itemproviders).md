# paste(itemProviders:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Performs a paste operation on the responder object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func paste(itemProviders: [NSItemProvider])
```

```objc
- (void) pasteItemProviders:(NSArray<NSItemProvider *> *) itemProviders;
```

## Discussion

This method performs a paste operation on the responder object, pasting the data provided by specified item providers.

## Parameters

- `itemProviders`: An array of [`NSItemProvider`](../../Foundation/nsitemprovider.md) objects.

## See Also

### Performing a paste operation
- [func canPaste([NSItemProvider]) -> Bool](./canpaste%28_%29.md)
  Returns a Boolean value that determines whether the responder object can perform a paste operation using data provided by the item providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfigurationsupporting/paste(itemproviders:))*