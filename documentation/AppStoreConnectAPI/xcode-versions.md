# Xcode Versions

**Framework**: App Store Connect API

Read Xcode version information you configure for an Xcode Cloud workflow.

#### Overview

The `ciXcodeVersions` resource represents the version of Xcode you configure for an Xcode Cloud workflow.

To change a workflow’s build environment, use the [`Workflows`](workflows.md) resource.

> **Note**:  This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

 This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Xcode Version Information
- [List All Xcode Versions Available in Xcode Cloud](get-v1-cixcodeversions.md)
  List all Xcode versions that are available to Xcode Cloud workflows.
- [Read Xcode Version Information](get-v1-cixcodeversions-_id_.md)
  Get information about a specific Xcode version that’s available to Xcode Cloud workflows.
- [List Available macOS Versions for an Xcode Version](get-v1-cixcodeversions-_id_-macosversions.md)
  List all macOS versions available in Xcode Cloud that support a specific Xcode version.
### Objects
- [object CiXcodeVersion](cixcodeversion.md)
  The data structure that represents an Xcode Versions resource.
- [object CiXcodeVersionResponse](cixcodeversionresponse.md)
  A response that contains a single Xcode Versions resource.
- [object CiXcodeVersionsResponse](cixcodeversionsresponse.md)
  A response that contains a list of Xcode Versions resources.

## See Also

- [Products](products.md)
  Read information about the products Xcode Cloud detected or delete a product and all its associated information.
- [Workflows](workflows.md)
  Manage Xcode Cloud workflows and view workflow details like actions and start conditions.
- [macOS Versions](macos-versions.md)
  Read macOS version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/xcode-versions)*