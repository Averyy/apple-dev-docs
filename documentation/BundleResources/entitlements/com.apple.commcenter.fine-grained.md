# com.apple.CommCenter.fine-grained

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that grants access to CoreTelephony services.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Details

- **Name**: `com.apple.CommCenter.fine-grained`
- **Type**: array of string 

## Possible Values

- `public-cellular-plan`: Add this value to discover whether a device supports eSIM, add a carrier eSIM, and update eSIM information using [`CTCellularPlanProvisioning`](../../CoreTelephony/ctcellularplanprovisioning.md). To request the entitlement with this value, fill out the [eSIM Access Entitlement request form](https://developer.apple.com/contact/request/esim-access-entitlement/).
- `public-subscriber-info`: Add this value to get information about a cellular network subscriber using [`CTSubscriber`](../../CoreTelephony/ctsubscriber.md). To request the entitlement with this value, fill out the [Carrier Refresh Token request form](https://developer.apple.com/contact/request/carrier-refresh-token/).

## Discussion

Add this entitlement to your app, and include specific values in the array, to use [Core Telephony](../../CoreTelephony/CoreTelephony.md) APIs. This entitlement is also available to App Clips. For more information about functionality available to App Clips, see [Choosing the right functionality for your App Clip](../../AppClip/choosing-the-right-functionality-for-your-app-clip.md).

To request this entitlement for your app, fill out the request form for the specific value you need to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.commcenter.fine-grained)*