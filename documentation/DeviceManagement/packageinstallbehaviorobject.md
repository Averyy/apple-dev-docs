# PackageInstallBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

A dictionary that describes how and when to install the package.

**Availability**:
- macOS 26.0+

## Declaration

```
object PackageInstallBehaviorObject
```

## Mentions

- [Installing packages](./installing-packages.md)

## Properties

- `Install` (string): A string that specifies when the system installs the package:

  - `Optional`: The user can install the package after the system activates the configuration.
  - `Required`: The system installs the package after it activates the configuration.

  **Default**: `Optional`; **Allowed Values**: `Optional`, `Required`

## See Also

### Objects
- [object PackageUninstallBehaviorObject](./packageuninstallbehaviorobject.md)
  A dictionary that describes how to uninstall the package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/packageinstallbehaviorobject)*