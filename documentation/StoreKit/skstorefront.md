# SKStorefront

**Framework**: Storekit  
**Kind**: class

An object containing the location and unique identifier of an Apple App Store storefront.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKStorefront
```

#### Overview

In-app products you create through App Store Connect are available for sale in every region with an App Store. You can use the storefront information to determine the customer’s region, and offer in-app products suitable for that region. StoreKit exposes [`SKStorefront`](skstorefront.md) storefront information as a read-only property in [`SKPaymentQueue`](skpaymentqueue.md).

You must maintain your own list of product identifiers and the storefronts in which you want to make them available.

> **Note**:  Don’t save the storefront information with your customer information; storefront information can change at any time. Always get the storefront identifier immediately before you display product information or availability to the customer in your app. Storefront information may not be used to develop or enhance a customer profile, or track customers for advertising or marketing purposes.

##### Show Products Based on the Current Storefront

The following example function `shouldShow` returns `false` if your product isn’t suitable for the given storefront. You must create your own list of products available by storefront, referred to as `myProducts` below:

```swift
func shouldShow(_ productIdentifier: String, in storefront: SKStorefront) -> Bool {
    var shouldShow = true
     
    // myProducts is a dictionary representing your own metadata for products,
    // keyed on an SKProduct.productIdentifier.
    if let myProduct = myProducts[productIdentifier] {
        shouldShow = myProduct.countryCodes.contains(storefront.countryCode)
    }
    return shouldShow
}
```

The following code listing requests information for products that you wish to display based on the device’s storefront. It uses the `shouldShow` function defined above.

```swift
func fetchProductInfo() {
    var identifiers = Set<String>()
    if let storefront = SKPaymentQueue.default().storefront {
        for (identifier, _) in myProducts {
            if shouldShow(identifier, in: storefront) {
                identifiers.insert(identifier)
            }
        }
        let request = SKProductsRequest(productIdentifiers: identifiers)
        request.delegate = self
        request.start()
    }
}
```

##### Listen for Storefront Changes

The storefront value can change at any time. To listen for changes in this value, implement the [`paymentQueueDidChangeStorefront(_:)`](skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:).md) method. The `shouldShow` function is defined in [`Show Products Based on the Current Storefront`](skstorefront#Show-Products-Based-on-the-Current-Storefront.md). Refresh the list of your available products when the storefront changes, as shown below:

```swift
func paymentQueueDidChangeStorefront(_ queue: SKPaymentQueue) {
    if let storefront = queue.storefront {
        // Refresh the displayed products based on the new storefront.
        for product in storeProducts {
            if shouldShow(product.productIdentifier, in: storefront) {
                // Display this product in your store UI.
         }
      }
   }
}
```

##### Respond to Storefront Changes

The current storefront can change at any time, including during a transaction. The following code listing determines whether the transaction should continue in the updated storefront. Your delegate’s [`paymentQueue(_:shouldContinue:in:)`](skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:).md) method must return quickly, before the call times out. The `shouldShow` function is defined in [`Show Products Based on the Current Storefront`](skstorefront#Show-Products-Based-on-the-Current-Storefront.md).

```swift
SKPaymentQueue.default().delegate = self  // Set your object as the SKPaymentQueue delegate.

func paymentQueue(_ paymentQueue: SKPaymentQueue,
                  shouldContinue transaction: SKPaymentTransaction,
                  in newStorefront: SKStorefront) -> Bool {
    return shouldShow(transaction.payment.productIdentifier, in: newStorefront)
}
```

If the product isn’t available in the updated storefront, the transaction fails with the error [`SKError.Code.storeProductNotAvailable`](skerror/code/storeproductnotavailable.md). Handle this error in your [`paymentQueue(_:updatedTransactions:)`](skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:).md) method by displaying an alert to let the customer know why the app can’t complete the transaction, as shown below:

```swift
func paymentQueue(_ queue: SKPaymentQueue,
                  updatedTransactions transactions: [SKPaymentTransaction]) {
    for transaction in transactions {
        if let transactionError = transaction.error as NSError?,
            transactionError.domain == SKErrorDomain
            && transactionError.code == SKError.storeProductNotAvailable.rawValue {
            // Show an alert.
        }
    }
}
```

##### Change the App Store Country or Region in the Sandbox Environment

When you change the App Store Country or Region in App Store Connect for a Sandbox Apple ID, it changes the storefront in your app. Change the region to test in-app purchases for different regions in your app. For more information about changing the App Store Country or Region in App Store Connect, see [`Test in-app purchases`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev7e89e149d).

> ❗ **Important**:  To successfully activate a storefront after you change the region in App Store Connect, sign out of the Sandbox Apple ID account on the device and sign back in.

## Topics

### Identifying the Storefront
- [var countryCode: String](skstorefront/countrycode.md)
  The three-letter code representing the country or region associated with the App Store storefront.
- [var identifier: String](skstorefront/identifier.md)
  A value defined by Apple that uniquely identifies an App Store storefront.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/skstorefront)*