# macOS Versions

**Framework**: App Store Connect API

Read macOS version information you configure for an Xcode Cloud workflow.

#### Overview

The `ciMacOsVersions` resource represents the version of macOS you configure for an Xcode Cloud workflow.

To change a workflow’s build environment, use the [`Workflows`](workflows.md) resource.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting macOS Version Information
- [List all macos versions available in xcode cloud](get-v1-cimacosversions.md)
  List all macOS versions available to Xcode Cloud workflows.
- [Read macos version information](get-v1-cimacosversions-_id_.md)
  Get information about a specific macOS version that’s available to Xcode Cloud workflows.
- [List available xcode versions for a macos version](get-v1-cimacosversions-_id_-xcodeversions.md)
  List all Xcode versions available for a specific macOS version in Xcode Cloud.
- [List Xcode version IDs for a CI macOS version](get-v1-cimacosversions-_id_-relationships-xcodeversions.md)
### Objects
- [object CiMacOsVersion](cimacosversion.md)
  A macOS version available in Xcode Cloud infrastructure for running workflow builds.
- [object CiMacOsVersionResponse](cimacosversionresponse.md)
  A response containing a single macOS version available in Xcode Cloud.
- [object CiMacOsVersionsResponse](cimacosversionsresponse.md)
  A response containing a list of macOS versions supported by Xcode Cloud.
- [object CiMacOsVersionXcodeVersionsLinkagesResponse](cimacosversionxcodeversionslinkagesresponse.md)

## See Also

- [Products](products.md)
  Read information about the products Xcode Cloud detected or delete a product and all its associated information.
- [Workflows](workflows.md)
  Manage Xcode Cloud workflows and view workflow details like actions and start conditions.
- [Xcode Versions](xcode-versions.md)
  Read Xcode version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/macos-versions)*