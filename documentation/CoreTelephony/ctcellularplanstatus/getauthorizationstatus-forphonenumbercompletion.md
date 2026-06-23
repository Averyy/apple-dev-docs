# getAuthorizationStatus(forPhoneNumber:completion:)

**Framework**: Core Telephony  
**Kind**: method

Returns the current authorization status for a phone number without presenting any UI.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class func authorizationStatus(forPhoneNumber phoneNumber: String) async throws -> CTCellularPlanStatusAuthorization
```

#### Discussion

Call this method before calling [`getHintForPhoneNumber(_:completion:)`](ctcellularplanstatus/gethintforphonenumber(_:completion:).md) to check whether the person already approved your app’s request to check cellular plan status for their phone number.

The completion handler receives the same [`CTCellularPlanStatusAuthorization`](ctcellularplanstatusauthorization.md) value as [`requestAuthorization(forPhoneNumber:completion:)`](ctcellularplanstatus/requestauthorization(forphonenumber:completion:).md), but without presenting UI.

## Parameters

- `phoneNumber`: A phone number in [`ITU-T E.164 international format`](https://developer.apple.comhttps://www.itu.int/rec/T-REC-E.164) (for example, `+15550001234`).
- `completionHandler`: A closure the framework calls with the current authorization status and any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/getauthorizationstatus(forphonenumber:completion:))*