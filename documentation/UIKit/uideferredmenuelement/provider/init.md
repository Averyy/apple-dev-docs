# init(_:)

**Framework**: UIKit  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
convenience init(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void)
```

## Parameters

- `elementProvider`: An asynchronous element provider block. Call this block’s completion handler when the responder’s   menu items are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uideferredmenuelement/provider/init(_:))*