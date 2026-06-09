# Xcode Versions

**Framework**: App Store Connect API

Read Xcode version information you configure for an Xcode Cloud workflow.

#### Overview

The `ciXcodeVersions` resource represents the version of Xcode you configure for an Xcode Cloud workflow.

To change a workflow’s build environment, use the [`Workflows`](workflows.md) resource.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Xcode Version Information
- [List all xcode versions available in xcode cloud](get-v1-cixcodeversions.md)
  List all Xcode versions that are available to Xcode Cloud workflows.
- [Read xcode version information](get-v1-cixcodeversions-_id_.md)
  Get information about a specific Xcode version that’s available to Xcode Cloud workflows.
- [List available macos versions for an xcode version](get-v1-cixcodeversions-_id_-macosversions.md)
  List all macOS versions available in Xcode Cloud that support a specific Xcode version.
- [List macOS version IDs for a CI Xcode version](get-v1-cixcodeversions-_id_-relationships-macosversions.md)
### Objects
- [object CiXcodeVersion](cixcodeversion.md)
  An Xcode version available in Xcode Cloud for running workflow builds and tests.
- [object CiXcodeVersionResponse](cixcodeversionresponse.md)
  The response body for endpoints that read a single Xcode version available in Xcode Cloud.
- [object CiXcodeVersionsResponse](cixcodeversionsresponse.md)
  The response body for endpoints that list Xcode versions available for Xcode Cloud.
- [object CiXcodeVersionMacOsVersionsLinkagesResponse](cixcodeversionmacosversionslinkagesresponse.md)

## See Also

- [Products](products.md)
  Read information about the products Xcode Cloud detected or delete a product and all its associated information.
- [Workflows](workflows.md)
  Manage Xcode Cloud workflows and view workflow details like actions and start conditions.
- [macOS Versions](macos-versions.md)
  Read macOS version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcode-versions)*