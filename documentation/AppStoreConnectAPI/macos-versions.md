# macOS Versions

**Framework**: Appstoreconnectapi

Read macOS version information you configure for an Xcode Cloud workflow.

#### Overview

The `ciMacOsVersions` resource represents the version of macOS you configure for an Xcode Cloud workflow.

To change a workflow’s build environment, use the [`Workflows`](workflows.md) resource.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting macOS Version Information
- [List All macOS Versions Available in Xcode Cloud](get-v1-cimacosversions.md)
  List all macOS versions available to Xcode Cloud workflows.
- [Read macOS Version Information](get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [List Available Xcode Versions for a macOS Version](get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.
### Objects
- [object CiMacOsVersion](cimacosversion.md)
  The data structure that represents a macOS Versions resource.
- [object CiMacOsVersionResponse](cimacosversionresponse.md)
  A response that contains a single macOS Versions resource.
- [object CiMacOsVersionsResponse](cimacosversionsresponse.md)
  A response that contains a list of macOS Versions resources.

## See Also

- [Products](products.md)
  Read information about the products Xcode Cloud detected or delete a product and all its associated information.
- [Workflows](workflows.md)
  Manage Xcode Cloud workflows and view workflow details like actions and start conditions.
- [Xcode Versions](xcode-versions.md)
  Read Xcode version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/macos-versions)*