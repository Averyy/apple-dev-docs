# Supporting business model changes by using the app transaction

**Framework**: Storekit

Access the app transaction to learn when a customer first purchased an app, to determine the app features they’re entitled to.

#### Overview

The [`originalAppVersion`](apptransaction/originalappversion.md) property indicates the app version that the customer purchased. If you change your business model from a paid app to a free app that offers in-app purchases, use this property to learn whether the customer purchased your app before you changed the business model. Then, use that information to determine your customers’ entitlement to features that were available in the paid app.

For example, an app that is a paid app in version 1 has premium features available to everyone who buys it. For version 2, the developer changes the business model, making it a free app that offers in-app purchases. Version 2 of the app has the same premium features, but now they’re available as in-app purchases.

In version 2, the developer wants to continue to provide the premium features to customers who purchased version 1. To do so, the app performs the following steps:

1. The app’s code includes a constant that indicates the version the business model changed; that constant is `"2"` in this example.
2. The app compares the [`originalAppVersion`](apptransaction/originalappversion.md)  value with the constant. If the customer purchased the app before the business model changed, the app determines that they’re entitled to the premium features.
3. The app also checks the [`currentEntitlements`](transaction/currententitlements.md) sequence and delivers any in-app purchases the customers may have made.

An app that performs these steps ensures that paid customers can access the premium features that were included with the app they purchased.

The code example below demonstrates how an app gets an [`AppTransaction`](apptransaction.md), compares the [`originalAppVersion`](apptransaction/originalappversion.md) with a constant that represents an app version, and determines the customer’s entitlements.

```swift
do {
    // Get the appTransaction.
    let shared = try await AppTransaction.shared
    if case .verified(let appTransaction) = shared {
        // Hard-code the major version number in which the app's business model changed.
        let newBusinessModelMajorVersion = "2" 

        // Get the major version number of the version the customer originally purchased.
        let versionComponents = appTransaction.originalAppVersion.split(separator: ".")
        let originalMajorVersion = versionComponents[0]

        if originalMajorVersion < newBusinessModelMajorVersion {
            // This customer purchased the app before the business model changed.
            // Deliver content that they're entitled to based on their app purchase.
        }
        else {
            // This customer purchased the app after the business model changed.
        }
    }
}
catch {
    // Handle errors.
}

// Iterate through any other products the customer purchased.
for await result in Transaction.currentEntitlements {
    if case .verified(let transaction) = result {
        // Deliver the content based on the customer's current entitlements.
    }
}
```

> **Note**:  Session 10007:  [`What’s new with in-app purchase`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10007/)

## See Also

- [struct AppTransaction](apptransaction.md)
  Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/supporting-business-model-changes-by-using-the-app-transaction)*