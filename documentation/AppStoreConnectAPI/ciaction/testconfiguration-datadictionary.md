# CiAction.TestConfiguration

**Framework**: App Store Connect API  
**Kind**: dictionary

The test configuration for a test action.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiAction.TestConfiguration
```

## Topics

### Objects and Types
- [object CiTestDestination](citestdestination.md)
  The test destination of a test action that Xcode Cloud performs.
- [type CiTestDestinationKind](citestdestinationkind.md)
  The string that represents the kind of a test destination.

## Properties

- `kind` (string): A string that describes whether the test action uses the scheme’s default tests or a specific test plan.
- `testDestinations` ([CiTestDestination]): A list of destination information for the test configuration.
- `testPlanName` (string): The name of the test plan. This value is only available to test actions that set the `kind` field to `SPECIFIC_TEST_PLANS`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciaction/testconfiguration-data.dictionary)*