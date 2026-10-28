# init(_:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void)
```

```objc
+ (instancetype) providerWithElementProvider:(void (^)(void (^completion)(NSArray<UIMenuElement *> *elements))) elementProvider;
```

## Discussion

Creates a deferred menu element provider with an asynchronous block.

## Parameters

- `elementProvider`: An asynchronous element provider block. Call this block’s completion handler when the responder’s menu items are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/provider/init(_:))*