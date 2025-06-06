# BrowserKit

**Framework**: BrowserKit  
**Kind**: module

Check a device’s eligibility to run alternative browser engines.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

#### Overview

Use BrowserKit to test whether a device is eligible to run a browser that uses an alternative browser engine, so your app can offer the alternative browser engine to a person. In your browser that uses WebKit, call [`isEligible(for:completionHandler:)`](beavailability/iseligible(for:completionhandler:).md) to test whether the device can run a version of your app that uses an alternative browser engine:

```swift
do {
  guard await BEAvailability.isEligible(for: .webBrowser) else {
    return
  }
  // Offer a person a marketplace link to your browser that uses an alternative browser engine.
}
catch let error {
  // Handle the error.
}
```

For more information on creating alternative browser engines, see [`Designing your browser architecture`](https://developer.apple.com/documentation/BrowserEngineKit/designing-your-browser-architecture).

## Topics

### Testing eligibility to use alternative browser engines
- [class BEAvailability](beavailability.md)
  A class that tests whether a device is eligible to run an alternative browser engine.
- [BEAvailability.Context](beavailability/context.md)
  The category of app for which you determine eligibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserKit)*