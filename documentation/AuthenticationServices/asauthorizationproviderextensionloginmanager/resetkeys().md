# resetKeys()

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Creates new encryption, signing, and Secure Enclave keys.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func resetKeys()
```

```objc
- (void) resetKeys;
```

## Discussion

This call permanently destroys the keys and you can’t undo it.

## See Also

### Repairing registrations
- [func userRegistrationsNeedsRepair()](./userregistrationsneedsrepair%28%29.md)
  Invokes the user registration to run again so the current user can repair it.
- [func deviceRegistrationsNeedsRepair()](./deviceregistrationsneedsrepair%28%29.md)
  Invokes the device registration to run again so the current user can repair it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/resetkeys())*