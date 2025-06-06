# Handling errors

**Framework**: StoreKit

Determine the underlying cause of errors that result from StoreKit requests.

#### Overview

A StoreKit request may fail for one of many possible reasons, including invalid product information, invalid payment details, problems with your App Store Connect account, or networking issues. When an error occurs, check the error code to find out what went wrong.

##### Determine the Cause of the Error

When handling errors, such as with the [`request(_:didFailWithError:)`](skrequestdelegate/request(_:didfailwitherror:).md) delegate method, it’s important to use the [`domain`](https://developer.apple.com/documentation/foundation/nserror/1413924-domain) and [`code`](https://developer.apple.com/documentation/foundation/nserror/1409165-code) of the resulting error to determine the underlying cause of failure.

StoreKit uses [`SKErrorDomain`](skerrordomain.md) for errors related to payments, store products, and cloud services, as described in [`SKError.Code`](skerror/code.md). For additional information on troubleshooting StoreKit framework issues, see the [`In-App Purchase FAQ`](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2413/_index.html#//apple_ref/doc/uid/DTS40016228).

Errors related to networking use [`NSURLErrorDomain`](https://developer.apple.com/documentation/Foundation/NSURLErrorDomain). The following table describes some of the most common networking errors that may occur when using StoreKit:

| Error code | Description |
| --- | --- |
| [`NSURLErrorTimedOut`](https://developer.apple.com/documentation/foundation/nsurlerrortimedout) (`-1001`) | The connection timed out. |
| [`NSURLErrorCannotFindHost`](https://developer.apple.com/documentation/foundation/nsurlerrorcannotfindhost) (`-1003`) | The connection failed because it can’t find the host. |
| [`NSURLErrorCannotConnectToHost`](https://developer.apple.com/documentation/foundation/nsurlerrorcannotconnecttohost) (`-1004`) | The connection failed because it can’t connect to the host. |
| [`NSURLErrorNetworkConnectionLost`](https://developer.apple.com/documentation/foundation/nsurlerrornetworkconnectionlost) (`-1005`) | The connection failed because it lost the network connection. |
| [`NSURLErrorNotConnectedToInternet`](https://developer.apple.com/documentation/foundation/nsurlerrornotconnectedtointernet) (`-1009`) | The connection failed because the device isn’t connected to the internet. |
| [`NSURLErrorUserCancelledAuthentication`](https://developer.apple.com/documentation/foundation/nsurlerrorusercancelledauthentication) (`-1012`) | The connection failed because the user canceled required authentication. |
| [`NSURLErrorSecureConnectionFailed`](https://developer.apple.com/documentation/foundation/nsurlerrorsecureconnectionfailed) (`-1200`) | The secure connection failed for an unknown reason. |

## See Also

- [SKError.Code](skerror/code.md)
  Error codes for StoreKit errors.
- [struct SKError](skerror.md)
  StoreKit error descriptions, codes, and domains.
- [let SKErrorDomain: String](skerrordomain.md)
  The error domain name for StoreKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/handling-errors)*