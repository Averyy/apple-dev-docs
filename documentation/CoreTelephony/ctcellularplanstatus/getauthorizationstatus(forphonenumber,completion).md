# getAuthorizationStatus(forPhoneNumber:completion:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Type Method

Returns the current authorization status for a phone number without presenting any UI.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class func getAuthorizationStatus(forPhoneNumber phoneNumber: String, completion completionHandler: @escaping @Sendable (CTCellularPlanStatusAuthorization, (any Error)?) -> Void)
```

```swift
class func authorizationStatus(forPhoneNumber phoneNumber: String) async throws -> CTCellularPlanStatusAuthorization
```

```objc
+ (void) getAuthorizationStatusForPhoneNumber:(NSString *) phoneNumber completion:(void (^)(CTCellularPlanStatusAuthorization status, NSError *error)) completionHandler;
```

## Discussion

Call this method before calling [`getHintForPhoneNumber(_:completion:)`](./gethintforphonenumber%28_,completion%29.md) to check whether the person already approved your app’s request to check cellular plan status for their phone number.

The completion handler receives the same [`CTCellularPlanStatusAuthorization`](../ctcellularplanstatusauthorization.md) value as [`requestAuthorization(forPhoneNumber:completion:)`](./requestauthorization%28forphonenumber,completion%29.md), but without presenting UI.

## Parameters

- `phoneNumber`: A phone number in [ITU-T E.164 international format](https://www.itu.int/rec/T-REC-E.164) (for example, `+15550001234`).
- `completionHandler`: A closure the framework calls with the current authorization status and any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/getauthorizationstatus(forphonenumber:completion:))*