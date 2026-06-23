# requestAuthorization(forPhoneNumber:completion:)

**Framework**: Core Telephony  
**Kind**: method

Presents a prompt that asks the person to allow cellular plan checks for their phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class func requestAuthorization(forPhoneNumber phoneNumber: String) async throws -> CTCellularPlanStatusAuthorization
```

#### Discussion

The completion handler receives a [`CTCellularPlanStatusAuthorization`](ctcellularplanstatusauthorization.md) value in the following circumstances:

- **[`CTCellularPlanStatusAuthorization.authorized`](ctcellularplanstatusauthorization/authorized.md)**: The person grants permission.
- **[`CTCellularPlanStatusAuthorization.notAuthorized`](ctcellularplanstatusauthorization/notauthorized.md)**: The person denies permission.
- **[`CTCellularPlanStatusAuthorization.restricted`](ctcellularplanstatusauthorization/restricted.md)**: Cellular plan checks aren’t available for the given number.

Only call [`getHintForPhoneNumber(_:completion:)`](ctcellularplanstatus/gethintforphonenumber(_:completion:).md) after receiving an [`CTCellularPlanStatusAuthorization.authorized`](ctcellularplanstatusauthorization/authorized.md) result.

## Parameters

- `phoneNumber`: A phone number in [`ITU-T E.164 international format`](https://developer.apple.comhttps://www.itu.int/rec/T-REC-E.164) (for example, `+15550001234`).
- `completionHandler`: A closure the framework calls with the authorization result and any error that occurs.

## See Also

- [enum CTCellularPlanStatusAuthorization](ctcellularplanstatusauthorization.md)
  Constants that indicate the authorization status for accessing cellular plan information for a phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/requestauthorization(forphonenumber:completion:))*