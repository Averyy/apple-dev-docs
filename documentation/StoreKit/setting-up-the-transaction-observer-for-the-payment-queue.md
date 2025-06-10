# Setting up the transaction observer for the payment queue

**Framework**: StoreKit

Enable your app to receive and handle transactions by adding an observer.

#### Overview

To process transactions in your app, you need to create and add an observer to the payment queue. The observer object responds to new transactions and synchronizes the queue of pending transactions with the App Store, and the payment queue prompts users to authorize payment. It’s important to add the transaction observer at app launch to ensure you don’t miss payment queue notifications that the system may send when the app launches.

##### Create an Observer

Create and build a custom observer class to handle changes to the payment queue.

```swift
class StoreObserver: NSObject, SKPaymentTransactionObserver {
                ....
    //Initialize the store observer.
    override init() {
        super.init()
        //Other initialization here.
    }

    //Observe transaction updates.
    func paymentQueue(_ queue: SKPaymentQueue,updatedTransactions transactions: [SKPaymentTransaction]) {
        //Handle transaction states here.
    }
                ....
}
```

Create an instance of this observer class to act as the observer of changes to the payment queue.

```swift
let iapObserver = StoreObserver()
```

> 💡 **Tip**:  Consider creating your observer as a shared instance of the class for global reference in any other class. A shared instance also ensures the lifetime of the object, so that the same instance handles callbacks for the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol.

After you create the transaction observer, you can add it to the payment queue.

##### Add an Observer

StoreKit attaches your observer to the queue when your app calls.

```swift
SKPaymentQueue.default().add(iapObserver)
```

StoreKit can notify your [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) instance automatically when the content of the payment queue changes upon resuming or while running your app.

Implement the transaction observer.

```swift
import UIKit
import StoreKit

class AppDelegate: UIResponder, UIApplicationDelegate {
                ....
    // Attach an observer to the payment queue.
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        SKPaymentQueue.default().add(iapObserver)
        return true
    }

    // The system calls this when the app is about to terminate.
    func applicationWillTerminate(_ application: UIApplication) {
        // Remove the observer.
        SKPaymentQueue.default().remove(iapObserver)
    }
                ....
}
```

It’s important to add the observer at launch, in [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)), to ensure that it persists during all launches of your app, receives all payment queue notifications, and continues transactions that may initiate outside the app, such as:

- Promoted in-app purchases. For more information, see [`Promoting In-App Purchases`](promoting-in-app-purchases.md).
- Background subscription renewals
- Interrupted purchases

The observer needs to be persistent so the system doesn’t deallocate it when it sends the app to the background. Only a persistent observer can receive transactions that may occur while your app is in the background, such as a renewal transaction for an auto-renewable subscription.

## See Also

- [func add(any SKPaymentTransactionObserver)](skpaymentqueue/add(_:)-5ciz2.md)
  Adds an observer to the payment queue.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [class SKPaymentQueue](skpaymentqueue.md)
  A queue of payment transactions for the App Store to process.
- [protocol SKPaymentTransactionObserver](skpaymenttransactionobserver.md)
  A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.
- [protocol SKPaymentQueueDelegate](skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.
- [class SKRequest](skrequest.md)
  An abstract class that represents a request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/setting-up-the-transaction-observer-for-the-payment-queue)*