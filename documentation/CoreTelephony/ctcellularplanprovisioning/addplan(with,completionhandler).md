# addPlan(with:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Instance Method

Starts the provisioning process for a specified eSIM.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func addPlan(with request: CTCellularPlanProvisioningRequest, completionHandler: @escaping @Sendable (CTCellularPlanProvisioningAddPlanResult) -> Void)
```

```swift
func addPlan(with request: CTCellularPlanProvisioningRequest) async -> CTCellularPlanProvisioningAddPlanResult
```

```objc
- (void) addPlanWith:(CTCellularPlanProvisioningRequest *) request completionHandler:(void (^)(CTCellularPlanProvisioningAddPlanResult result)) completionHandler;
```

#### Discussion

Once your app calls this method, an iOS wizard guides the user through the process of installing and configuration an eSIM.

##### Installing an eSIM in the Background

The user may send your app to the background prior to completing eSIM installation. To ensure your app has an opportunity to execute the completion handler and get the result of the installation, use [`beginBackgroundTask(expirationHandler:)`](../../UIKit/uiapplication/beginbackgroundtask%28expirationhandler%29.md) to perform the eSIM installation as a background task.

## Parameters

- `request`: A [`CTCellularPlanProvisioningRequest`](../ctcellularplanprovisioningrequest.md) that identifies the eSIM to download.
- `completionHandler`: A completion handler that executes after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

### Provisioning an eSIM
- [func supportsCellularPlan() -> Bool](./supportscellularplan%28%29.md)
  Returns whether the device and your app meet eSIM provisioning requirements.
- [var supportsEmbeddedSIM: Bool](./supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./addplan%28request,properties,completionhandler%29.md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](../ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/addplan(with:completionhandler:))*