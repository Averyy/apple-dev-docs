# applicationShouldRequestHealthAuthorization(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when your app should ask the user for access to his or her HealthKit data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func applicationShouldRequestHealthAuthorization(_ application: UIApplication)
```

```objc
- (void) applicationShouldRequestHealthAuthorization:(UIApplication *) application;
```

## Discussion

In your implementation of this method, call the [`handleAuthorizationForExtension(completion:)`](../../HealthKit/hkhealthstore/handleauthorizationforextension%28completion%29.md) method of the [`HKHealthStore`](../../HealthKit/hkhealthstore.md) object.

## Parameters

- `application`: Your singleton app object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationshouldrequesthealthauthorization(_:))*