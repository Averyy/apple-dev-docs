# supportsCellularPlan()

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Instance Method

Returns whether the device and your app meet eSIM provisioning requirements.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func supportsCellularPlan() -> Bool
```

```objc
- (BOOL) supportsCellularPlan;
```

## Return Value

[`true`](../../Swift/true.md) if all requirements are met; otherwise [`false`](../../Swift/false.md).

## Discussion

This method returns [`true`](../../Swift/true.md) when all of the following conditions are met:

- The device supports eSIM installation.
- The activation policy allows eSIM installation.
- Your app includes the [`com.apple.CommCenter.fine-grained`](../../BundleResources/entitlements/com.apple.commcenter.fine-grained.md) entitlement with `public-cellular-plan` in its array of values.

You can use this method to verify that your entitlement is properly configured. If you expect the device to support cellular plans but it returns [`false`](../../Swift/false.md), check that you’ve added the required entitlement to your app and that its value array includes `public-cellular-plan`.

This method doesn’t check whether you have installed an eSIM. You can call this method at any time.

## See Also

### Provisioning an eSIM
- [var supportsEmbeddedSIM: Bool](./supportsembeddedsim.md)
  A Boolean value that indicates whether the device has hardware eSIM support.
- [func addPlan(request: CTCellularPlanProvisioningRequest, properties: CTCellularPlanProperties?, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./addplan%28request,properties,completionhandler%29.md)
  Starts the provisioning process with optional properties for the specified eSIM.
- [func addPlan(with: CTCellularPlanProvisioningRequest, completionHandler: (CTCellularPlanProvisioningAddPlanResult) -> Void)](./addplan%28with,completionhandler%29.md)
  Starts the provisioning process for a specified eSIM.
- [enum CTCellularPlanProvisioningAddPlanResult](../ctcellularplanprovisioningaddplanresult.md)
  The result from attempting to provision an eSIM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning/supportscellularplan())*