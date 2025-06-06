# NSHealthRequiredReadAuthorizationTypeIdentifiers

**Framework**: Bundle Resources  
**Kind**: typealias

The clinical record data types that your app must get permission to read.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- visionOS 1.0+

#### Discussion

Use this key to indicate that your app requires access to specific clinical record data types to function properly. Set the value to an array of strings containing the type identifiers for your required types. For a list of type identifiers, see [`HKClinicalTypeIdentifier`](https://developer.apple.com/documentation/HealthKit/HKClinicalTypeIdentifier).

To protect the user’s privacy, you must specify three or more required clinical record types. If the user denies authorization to any of the types, authorization fails with an [`HKError.Code.errorRequiredAuthorizationDenied`](https://developer.apple.com/documentation/HealthKit/HKError/Code/errorRequiredAuthorizationDenied) error. Your app is not told the record types to which the user denied access.

## See Also

- [Setting up HealthKit](../HealthKit/setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [NSHealthClinicalHealthRecordsShareUsageDescription](information-property-list/nshealthclinicalhealthrecordsshareusagedescription.md)
  A message to the user that explains why the app requested permission to read clinical records.
- [NSHealthShareUsageDescription](information-property-list/nshealthshareusagedescription.md)
  A message to the user that explains why the app requested permission to read samples from the HealthKit store.
- [NSHealthUpdateUsageDescription](information-property-list/nshealthupdateusagedescription.md)
  A message to the user that explains why the app requested permission to save samples to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthrequiredreadauthorizationtypeidentifiers)*