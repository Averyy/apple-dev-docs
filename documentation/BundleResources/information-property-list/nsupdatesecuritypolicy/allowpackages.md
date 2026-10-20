# AllowPackages

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of Team IDs that the system uses to determine whether an installer package, signed by one of the specified Team IDs, can update an app’s bundle.

**Availability**:
- macOS 13.0+

## Details

- **Name**: `AllowPackages`
- **Type**: array of string 

## See Also

### Related Documentation
- [NSUpdateSecurityPolicy](../nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
### Security policies
- [AllowProcesses](./allowprocesses.md)
  A dictionary that maps Team IDs to an array of signing (bundle) IDs that the system uses to determine whether a process can update an app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsupdatesecuritypolicy/allowpackages)*