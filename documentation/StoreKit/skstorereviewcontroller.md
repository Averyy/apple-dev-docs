# SKStoreReviewController

**Framework**: StoreKit  
**Kind**: class

An object that controls the process of requesting App Store ratings and reviews from customers.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class SKStoreReviewController
```

#### Overview

Use the [`requestReview(in:)`](skstorereviewcontroller/requestreview(in:).md) method to indicate when it makes sense within the logic of your app to ask the customer for ratings and reviews.

## Topics

### Indicating an appropriate time for a review
- [class func requestReview(in: UIWindowScene)](skstorereviewcontroller/requestreview(in:).md)
  Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene.
- [class func requestReview()](skstorereviewcontroller/requestreview.md)
  Tells StoreKit to ask the customer to rate or review your app, if appropriate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Requesting App Store reviews](requesting-app-store-reviews.md)
  Implement best practices for prompting users to review your app in the App Store.
- [struct RequestReviewAction](requestreviewaction.md)
  An instance that tells StoreKit to request an App Store rating or review, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorereviewcontroller)*