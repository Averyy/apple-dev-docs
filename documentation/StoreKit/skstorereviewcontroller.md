# SKStoreReviewController

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

An object that controls the process of requesting App Store ratings and reviews from customers.

**Availability**:
- iOS 10.3+ - Deprecated in 18.0
- iPadOS 10.3+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`RequestReviewAction`](./requestreviewaction.md) instead.

## Declaration

```swift
class SKStoreReviewController
```

```objc
@interface SKStoreReviewController : NSObject
```

#### Overview

Use the [`requestReview(in:)`](./skstorereviewcontroller/requestreview%28in%29.md) method to indicate when it makes sense within the logic of your app to ask the customer for ratings and reviews.

## Topics

### Indicating an appropriate time for a review
- [class func requestReview(in: UIWindowScene)](./skstorereviewcontroller/requestreview%28in%29.md)
  Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene.
- [class func requestReview()](./skstorereviewcontroller/requestreview%28%29.md)
  Tells StoreKit to ask the customer to rate or review your app, if appropriate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reviews
- [Requesting App Store reviews](./requesting-app-store-reviews.md)
  Implement best practices for prompting users to review your app in the App Store.
- [struct RequestReviewAction](./requestreviewaction.md)
  An instance that tells StoreKit to request an App Store rating or review, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorereviewcontroller)*