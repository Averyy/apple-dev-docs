# requestReview()

**Framework**: Storekit  
**Kind**: method

Tells StoreKit to ask the customer to rate or review your app, if appropriate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.14+

## Declaration

```swift
class func requestReview()
```

#### Discussion

Although you normally call this method when it makes sense in the user experience flow of your app, App Store policy governs the actual display of a rating and review request view. Because this method may not present an alert, it isn’t appropriate to call [`requestReview()`](skstorereviewcontroller/requestreview().md) or [`requestReview(in:)`](skstorereviewcontroller/requestreview(in:).md) in response to a button tap or other user action.

> **Note**:  When you call this method while your app is in development mode, a rating and review request view is always displayed so you can test the user interface and experience. However, this method has no effect when you call it in an app that you distribute using TestFlight.

When you call this method in your shipping app and the system displays a rating and review request view, the system handles the entire process for you. In addition, you can continue to include a persistent link in the settings or configuration screens of your app that links to your App Store product page. To automatically open a page on which users can write a review in the App Store, append the query parameter `action=write-review` to your product URL.

## See Also

- [class func requestReview(in: UIWindowScene)](skstorereviewcontroller/requestreview(in:).md)
  Tells StoreKit to ask the customer to rate or review the app, if appropriate, using the specified scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstorereviewcontroller/requestreview())*