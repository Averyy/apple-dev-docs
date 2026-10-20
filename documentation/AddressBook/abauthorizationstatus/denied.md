# ABAuthorizationStatus.denied

**Framework**: Address Book  
**Kind**: case  
**Role**: Case

The user explicitly denied access to address book data for this app.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use CNAuthorizationStatus

## Declaration

```swift
case denied
```

```c
kABAuthorizationStatusDenied
```

## See Also

### Constants
- [ABAuthorizationStatus.notDetermined](./notdetermined.md)
  No authorization status could be determined.
- [ABAuthorizationStatus.restricted](./restricted.md)
  The app is not authorized to access address book data. The user cannot change this access, possibly due to restrictions such as parental controls.
- [ABAuthorizationStatus.authorized](./authorized.md)
  The app is authorized to access address book data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abauthorizationstatus/denied)*