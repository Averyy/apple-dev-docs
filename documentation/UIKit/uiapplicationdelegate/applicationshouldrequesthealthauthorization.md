# applicationShouldRequestHealthAuthorization(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when your app should ask the user for access to his or her HealthKit data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationShouldRequestHealthAuthorization(_ application: UIApplication)
```

#### Discussion

In your implementation of this method, call the [`handleAuthorizationForExtension(completion:)`](https://developer.apple.com/documentation/HealthKit/HKHealthStore/handleAuthorizationForExtension(completion:)) method of the [`HKHealthStore`](https://developer.apple.com/documentation/HealthKit/HKHealthStore) object.

## Parameters

- `application`: Your singleton app object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationshouldrequesthealthauthorization(_:))*