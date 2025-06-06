# prepareStoreAndForward()

**Framework**: ProximityReader  
**Kind**: method

Configures the pipeline for reading payment or loyalty cards in Store and Forward mode.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
func prepareStoreAndForward() async throws -> StoreAndForwardPaymentCardReaderSession
```

#### Return Value

[`StoreAndForwardPaymentCardReaderSession`](storeandforwardpaymentcardreadersession.md) when successful.

#### Discussion

Call this function to configure Tap to Pay on iPhone on someone’s device. This method verifies that the device is able to read contactless cards and is properly configured to process reads in Store and Forward mode.

Prior to calling this method, make sure that your service provider has the Store and Forward feature enabled and that you created an online session in the last 24 hours.

> **Note**: [`PaymentCardReaderError`](paymentcardreadererror.md) if the method fails to configure the device.

[`PaymentCardReaderError`](paymentcardreadererror.md) if the method fails to configure the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/preparestoreandforward())*