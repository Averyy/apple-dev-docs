# addPlan(request:properties:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method

Starts the provisioning process with optional properties for the specified eSIM.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?) async -> CTCellularPlanProvisioningAddPlanResult
```

#### Overview

Provide the system the information needed for the existing API to perform an install with a [`CTCellularPlanProvisioningRequest`](ctcellularplanprovisioningrequest.md). By providing the request and properties object together, the system can pair the information together.

Once your app calls this method, an iOS wizard guides the person through the process of installing and configuration an eSIM.

The person may send your app to the background prior to completing eSIM installation. To ensure your app has an opportunity to execute the completion handler and get the result of the installation, use [`beginBackgroundTask(expirationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/beginBackgroundTask(expirationHandler:)) to perform the eSIM installation as a background task.

## Parameters

- `request`: A   that identifies the eSIM to download.
- `properties`: An optional parameter for  . Use to specify the voice capability and region your eSIM supports.
- `completionHandler`: A completion handler that executes after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

- [func supportsCellularPlan() -> Bool](ctcellularplanprovisioning/supportscellularplan.md)
  Indicates whether the device supports eSIM and the activation policy allows eSIM installation.
- [var supportsEmbeddedSIM: Bool](ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](ctcellularplanprovisioning/addplan(with:completionhandler:).md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/addplan(request:properties:completionhandler:))*