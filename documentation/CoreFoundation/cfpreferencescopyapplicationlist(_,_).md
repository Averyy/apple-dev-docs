# CFPreferencesCopyApplicationList(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Unsupported API

## Declaration

```swift
func CFPreferencesCopyApplicationList(_ userName: CFString, _ hostName: CFString) -> CFArray?
```

```c
extern CFArrayRefCFPreferencesCopyApplicationList(CFStringRef userName, CFStringRef hostName);
```

## Return Value

The list of application IDs. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `userName`: [`kCFPreferencesCurrentUser`](./kcfpreferencescurrentuser.md) to search the current-user domain, otherwise [`kCFPreferencesAnyUser`](./kcfpreferencesanyuser.md) to search the any-user domain.
- `hostName`: [`kCFPreferencesCurrentHost`](./kcfpreferencescurrenthost.md) to search the current-host domain, otherwise [`kCFPreferencesAnyHost`](./kcfpreferencesanyhost.md) to search the any-host domain.

## See Also

### Miscellaneous Functions
- [func CFPreferencesAppValueIsForced(CFString, CFString) -> Bool](./cfpreferencesappvalueisforced%28_,_%29.md)
  Determines whether or not a given key has been imposed on the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopyapplicationlist(_:_:))*