# update(_:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method

Updates the capability and region availability for an eSIM.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func update(_ properties: CTCellularPlanProperties) async throws
```

#### Overview

When you can’t call [`addPlan(request:properties:completionHandler:)`](ctcellularplanprovisioning/addplan(request:properties:completionhandler:).md) because a person installs your SIM with a QR Code, a universal link, or a physical SIM, use this method to issue eSIM property information for a particular eSIM before provisioning begins. Use the `associatedIccid` so that the system can match the future install with your provided property information.

You can also use this method to update information on an ICCID that already exists on the device. After matching the `associatedICCID`, the system updates the eSIM with the information you provide.

## Parameters

- `properties`: A required parameter where you specify the eSIM’s  ,   and  . If missing, an error is returned. You are allowed to provide an empty list for  .
- `completionHandler`: A completion handler that executes after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/update(_:completionhandler:))*