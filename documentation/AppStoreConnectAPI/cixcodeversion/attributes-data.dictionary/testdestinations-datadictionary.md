# CiXcodeVersion.Attributes.TestDestinations

**Framework**: App Store Connect API  
**Kind**: dictionary

The test destinations available for an Xcode version.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiXcodeVersion.Attributes.TestDestinations
```

## Topics

### Objects
- [object CiXcodeVersion.Attributes.TestDestinations.AvailableRuntimes](cixcodeversion/attributes-data.dictionary/testdestinations-data.dictionary/availableruntimes-data.dictionary.md)
  The data structure that represents the available runtimes for test destinations of an Xcode Versions resource.

## Properties

- `availableRuntimes` ([CiXcodeVersion.Attributes.TestDestinations.AvailableRuntimes]): A list of runtimes available for the Xcode version.
- `deviceTypeIdentifier` (string): A string that uniquely identifies the simulated device Xcode Cloud uses for a test action; for example, `com.apple.CoreSimulator.SimDeviceType.iPhone-12`.
- `deviceTypeName` (string): The display name of the simulated device Xcode Cloud uses for a test action; for example, `iPhone 12`.
- `kind` (CiTestDestinationKind): A string that indicates whether a test destination is a simulated device or a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cixcodeversion/attributes-data.dictionary/testdestinations-data.dictionary)*