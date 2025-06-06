# Activation Lock a Device

**Framework**: Device Management  
**Kind**: httpRequest

Enable activation lock on a remote device.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Find My iPhone Activation Lock is a feature of iCloud and Automated Device Enrollment that makes it harder for anyone to use or resell a lost or stolen iOS device. Activation Lock is a feature of iCloud, and MDM has the ability to allow users to enable the feature on Supervised devices.

There are two ways to manage Activation Lock: the Activation Lock request is available for devices that appear in the Apple School Manager portal or Apple Business Manager portal, or the Find My approach. Whichever method is the first to enable Activation Lock takes precedence.

## Topics

### Request and Response
- [object ActivationLockRequest](activationlockrequest.md)
  Request enabling activation lock for a device.
- [object ActivationLockStatusResponse](activationlockstatusresponse.md)
  The response to a request for activation lock.
### Bypass Codes
- [Creating and Using Bypass Codes](creating-and-using-bypass-codes.md)
  Maintain the bypass code parameters for disabling Activation Lock.

## Request Body

Request enabling activation lock for a device.

## See Also

- [Get Device Details](device-details.md)
  Get the details on a set of devices.
- [Get a List of Devices](fetch-devices.md)
  Get a list of devices that are managed by the server.
- [Sync the List of Devices](sync-devices.md)
  Get updates about the list of devices the server manages.
- [Disown Devices](disown-devices.md)
  Notify Apple’s servers that your organization no longer owns the specified devices.
- [Get Beta Enrollment Tokens](get-beta-enrollment-tokens.md)
  Retrieves the beta enrollment tokens available for the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activation-lock-devices)*