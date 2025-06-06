# addPlan(with:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method

Starts the provisioning process for a specified eSIM.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func addPlan(with request: CTCellularPlanProvisioningRequest) async -> CTCellularPlanProvisioningAddPlanResult
```

#### Discussion

Once your app calls this method, an iOS wizard guides the user through the process of installing and configuration an eSIM.

##### Installing an Esim in the Background

The user may send your app to the background prior to completing eSIM installation. To ensure your app has an opportunity to execute the completion handler and get the result of the installation, use [`beginBackgroundTask(expirationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/beginBackgroundTask(expirationHandler:)) to perform the eSIM installation as a background task.

## Parameters

- `request`: A   that identifies the eSIM to download.
- `completionHandler`: A completion handler that executes after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

- [func supportsCellularPlan() -> Bool](ctcellularplanprovisioning/supportscellularplan.md)
  Indicates whether the device supports eSIM and the activation policy allows eSIM installation.
- [var supportsEmbeddedSIM: Bool](ctcellularplanprovisioning/supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [enum CTCellularPlanProvisioningAddPlanResult](ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/addplan(with:completionhandler:))*