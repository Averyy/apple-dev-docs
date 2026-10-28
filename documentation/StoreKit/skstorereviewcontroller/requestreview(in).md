# requestReview(in:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use AppStore.requestReview(in:).

## Declaration

```swift
@MainActor
class func requestReview(in windowScene: UIWindowScene)
```

```objc
+ (void) requestReviewInScene:(UIWindowScene *) windowScene;
```

## Discussion

When you call this method in your shipping app and the system displays a rating and review request view, the system handles the entire process for you. Although you normally call this method when it makes sense in the user experience flow of your app, App Store policy governs the actual display of a rating and review request view. When your app calls this API, StoreKit uses the following criteria::

- If the person hasn’t rated or reviewed your app on this device, StoreKit displays the ratings and review request a maximum of three times within a 365-day period.
- If the person has rated or reviewed your app on this device, StoreKit displays the ratings and review request if the app version is new, and if more than 365 days have passed since the person’s previous review.

> **Note**:  Because this method may not present an alert, don’t call [`requestReview()`](./requestreview%28%29.md) or [`requestReview(in:)`](./requestreview%28in%29.md) in response to a button tap or other user action.

It’s up to your app to decide on the best timing for requesting reviews. For design guidance, see Human Interface Guidelines > [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews).

### Test review requests

When your app calls this method while it’s in development mode, StoreKit always displays the rating and review request view, so you can test the user interface and experience. However, this method has no effect in apps that you distribute for beta testing using TestFlight.

### Provide a persistent link to your product page (optional)

Your customers can review your app at any time on the App Store. To make it easier for people to leave reviews, you may include a persistent link to your App Store product page in your app’s settings or configuration screens. Append the query parameter `action=write-review` to your product page URL to automatically open the App Store page where users can write a review.

## Parameters

- `windowScene`: The window scene that StoreKit uses to present the rating and review request interface.

## See Also

### Indicating an appropriate time for a review
- [class func requestReview()](./requestreview%28%29.md)
  Tells StoreKit to ask the customer to rate or review your app, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorereviewcontroller/requestreview(in:))*