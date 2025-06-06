# resetKeys()

**Framework**: Authentication Services  
**Kind**: method

Creates new encryption, signing, and Secure Enclave keys for the user.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func resetKeys()
```

#### Discussion

This call permanently destroys the keys and you can’t undo it.

## See Also

- [func userRegistrationsNeedsRepair()](asauthorizationproviderextensionloginmanager/userregistrationsneedsrepair.md)
  Invokes the user registration to run again so the current user can repair it.
- [func deviceRegistrationsNeedsRepair()](asauthorizationproviderextensionloginmanager/deviceregistrationsneedsrepair.md)
  Invokes the device registration to run again so the current user can repair it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/resetkeys())*