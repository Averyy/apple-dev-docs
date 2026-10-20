# NSHealthRequiredReadAuthorizationTypeIdentifiers

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The clinical record data types that your app must get permission to read.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- visionOS 1.0+

## Details

- **Name**: `NSHealthRequiredReadAuthorizationTypeIdentifiers`
- **Type**: array of string 

#### Discussion

Use this key to indicate that your app requires access to specific clinical record data types to function properly. Set the value to an array of strings containing the type identifiers for your required types. For a list of type identifiers, see [`HKClinicalTypeIdentifier`](../../HealthKit/hkclinicaltypeidentifier.md).

To protect the user’s privacy, you must specify three or more required clinical record types. If the user denies authorization to any of the types, authorization fails with an [`HKError.Code.errorRequiredAuthorizationDenied`](../../HealthKit/hkerror/code/errorrequiredauthorizationdenied.md) error. Your app is not told the record types to which the user denied access.

## See Also

### Health
- [Setting up HealthKit](../../HealthKit/setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [NSHealthClinicalHealthRecordsShareUsageDescription](./nshealthclinicalhealthrecordsshareusagedescription.md)
  A message to the user that explains why the app requested permission to read clinical records.
- [NSHealthShareUsageDescription](./nshealthshareusagedescription.md)
  A message that explains to people why the app requests permission to read samples from the HealthKit store.
- [NSHealthUpdateUsageDescription](./nshealthupdateusagedescription.md)
  A message to the user that explains why the app requested permission to save samples to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthrequiredreadauthorizationtypeidentifiers)*