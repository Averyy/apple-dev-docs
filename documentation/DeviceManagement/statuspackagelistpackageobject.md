# StatusPackageListPackageObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a declarative package.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object StatusPackageListPackageObject
```

## Topics

### Objects
- [object StatusPackageListStatusReasonObject](statuspackageliststatusreasonobject.md)
  Information about a status error.

## Properties

- `_removed` (boolean): If `true`, the system removed the package and only this key and the `identifier` key are present in the status item object.
- `declaration-identifier` (string): The identifier of the declaration that controls the package.
- `identifier` (string) *(required)*: The package’s unique identifier. This is the package identifier value of the package file.
- `name` (string): The name of the package.
- `reasons` ([StatusPackageListStatusReasonObject]): An array that contains additional details about the package state, including errors.
- `state` (string): The status of the package, which has the following possible values: - `optional`: The package is optional and the user has to trigger its installation.
- `queued`: Installation of the package has started.
- `prompting-for-consent`: The system is displaying a prompt to the user to proceed with package installation.
- `downloading`: The system is downloading the package.
- `installing`: The system is installing the package.
- `installed`: The package is installed.
- `failed`: The package install failed.
- `version` (string): The version of the package. This will be the package version value of the package file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspackagelistpackageobject)*