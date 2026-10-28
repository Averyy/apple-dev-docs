# HKAuthorizationStatus

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the authorization status for a particular data type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKAuthorizationStatus
```

```c
enum HKAuthorizationStatus : NSInteger;
```

## Overview

This status indicates whether  the user has authorized your app to save data of the given type.

To help maintain the privacy of sensitive health data, HealthKit does not tell you when the user denies your app permission to query data. Instead, it simply appears as if HealthKit does not have any data matching your query. Your app will receive only the data that it has written to HealthKit. Data from other sources remains hidden from your app. For more information on privacy in HealthKit, see `HealthKit`.

## Topics

### Constants
- [HKAuthorizationStatus.notDetermined](./hkauthorizationstatus/notdetermined.md)
  The user has not yet chosen to authorize access to the specified data type.
- [HKAuthorizationStatus.sharingDenied](./hkauthorizationstatus/sharingdenied.md)
  The user has explicitly denied your app permission to save data of the specified type.
- [HKAuthorizationStatus.sharingAuthorized](./hkauthorizationstatus/sharingauthorized.md)
  The user has explicitly authorized your app to save data of the specified type.
### Initializers
- [init?(rawValue: Int)](./hkauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing HealthKit
- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](./hkhealthstore/authorizationstatus%28for%29.md)
  Returns the app’s authorization status for sharing the specified data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](./hkhealthstore/getrequeststatusforauthorization%28toshare,read,completion%29.md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](./hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
- [class func isHealthDataAvailable() -> Bool](./hkhealthstore/ishealthdataavailable%28%29.md)
  Returns a Boolean value that indicates whether HealthKit is available on this device.
- [func supportsHealthRecords() -> Bool](./hkhealthstore/supportshealthrecords%28%29.md)
  Returns a Boolean value that indicates whether the current device supports clinical records.
- [func requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/requestauthorization%28toshare,read,completion%29.md)
  Requests permission to save and read the specified data types.
- [func requestAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>) async throws](./hkhealthstore/requestauthorization%28toshare,read%29.md)
  Asynchronously requests permission to save and read the specified data types.
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/requestperobjectreadauthorization%28for,predicate,completion%29.md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/handleauthorizationforextension%28completion%29.md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](./hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.
- [func getEarliestAuthorizedSampleDate(for: Set<HKObjectType>, completion: ([HKObjectType : Date]?, (any Error)?) -> Void)](./hkhealthstore/getearliestauthorizedsampledate%28for,completion%29.md)
  Returns the earliest date that the person permits your app to read samples for the given data types.
- [func earliestPermittedSampleDate() -> Date](./hkhealthstore/earliestpermittedsampledate%28%29.md)
  Returns the earliest date that the framework permits your app to save or read samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus)*