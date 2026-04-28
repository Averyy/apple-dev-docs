# PackageInstallBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies the install behavior of the package.

**Availability**:
- macOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PackageInstallBehaviorObject
```

## Mentions

- [Installing packages](installing-packages.md)

## Properties

- `Install` (string): A string that specifies when the system installs the package: - `Optional`: The user can install the package after the system activates the configuration.
- `Required`: The system installs the package after it activates the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/packageinstallbehaviorobject)*