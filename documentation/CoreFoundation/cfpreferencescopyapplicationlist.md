# CFPreferencesCopyApplicationList(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFPreferencesCopyApplicationList(_ userName: CFString, _ hostName: CFString) -> CFArray?
```

#### Return Value

The list of application IDs. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `userName`:   to search the current-user domain, otherwise   to search the any-user domain.
- `hostName`:   to search the current-host domain, otherwise   to search the any-host domain.

## See Also

- [func CFPreferencesAppValueIsForced(CFString, CFString) -> Bool](cfpreferencesappvalueisforced(_:_:).md)
  Determines whether or not a given key has been imposed on the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopyapplicationlist(_:_:))*