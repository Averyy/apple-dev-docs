# managementURL

**Framework**: Apple Pay on the Web  
**Kind**: property

A URL to a web page where the user can update or delete the payment method for the automatic reload payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString managementURL;
```

#### Discussion

When users remove a payment method, the system deletes the associated Apple Pay merchant token.

> **Note**:  It’s a best practice to use a universal link for this URL. Using a universal link, the same link can direct a person to a page in the app (if they’ve installed the app) or to a page on the merchant’s web site. For more information on adopting universal links, see [`Universal links`](https://developer.apple.comhttps://developer.apple.com/ios/universal-links/).

 It’s a best practice to use a universal link for this URL. Using a universal link, the same link can direct a person to a page in the app (if they’ve installed the app) or to a page on the merchant’s web site. For more information on adopting universal links, see [`Universal links`](https://developer.apple.comhttps://developer.apple.com/ios/universal-links/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest/managementurl)*