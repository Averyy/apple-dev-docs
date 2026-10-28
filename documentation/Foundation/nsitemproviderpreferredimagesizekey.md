# NSItemProviderPreferredImageSizeKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A key provided to the options dictionary to indicate a preferred image size.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSItemProviderPreferredImageSizeKey: String
```

```c
extern NSString * const NSItemProviderPreferredImageSizeKey;
```

## Discussion

Use this key only with the [`NSItemProvider`](./nsitemprovider.md) type coercion policy. Ensure the value is an [`NSValue`](./nsvalue.md) object that contains a [`CGSize`](../CoreFoundation/cgsize.md) struct specifying the requested size, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderpreferredimagesizekey)*