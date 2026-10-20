# AllowProcesses

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

A dictionary that maps Team IDs to an array of signing (bundle) IDs that the system uses to determine whether a process can update an app’s bundle.

**Availability**:
- macOS 13.0+

## Details

- **Name**: `AllowProcesses`
- **Type**: dictionary

## See Also

### Related Documentation
- [NSUpdateSecurityPolicy](../nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
### Security policies
- [AllowPackages](./allowpackages.md)
  An array of Team IDs that the system uses to determine whether an installer package, signed by one of the specified Team IDs, can update an app’s bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsupdatesecuritypolicy/allowprocesses)*