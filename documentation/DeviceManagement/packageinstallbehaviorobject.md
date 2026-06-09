# PackageInstallBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes how and when to install the package.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object PackageInstallBehaviorObject
```

## Mentions

- [Installing packages](installing-packages.md)

## Properties

- `Install` (string): A string that specifies when the system installs the package: - `Optional`: The user can install the package after the system activates the configuration.
- `Required`: The system installs the package after it activates the configuration.

## See Also

- [object PackageUninstallBehaviorObject](packageuninstallbehaviorobject.md)
  A dictionary that describes how to uninstall the package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/packageinstallbehaviorobject)*