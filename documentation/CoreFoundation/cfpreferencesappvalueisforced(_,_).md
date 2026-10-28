# CFPreferencesAppValueIsForced(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Determines whether or not a given key has been imposed on the user.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFPreferencesAppValueIsForced(_ key: CFString, _ applicationID: CFString) -> Bool
```

```c
extern Boolean CFPreferencesAppValueIsForced(CFStringRef key, CFStringRef applicationID);
```

## Return Value

`true` if value of the key cannot be changed by the user, otherwise `false`.

## Discussion

In cases where machines and/or users are under some kind of management, you should use this function to determine whether or not to disable UI elements corresponding to those preference keys.

## Parameters

- `key`: The key you are querying.
- `applicationID`: The application’s ID, typically [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](./kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## See Also

### Miscellaneous Functions
- [func CFPreferencesCopyApplicationList(CFString, CFString) -> CFArray?](./cfpreferencescopyapplicationlist%28_,_%29.md)
  Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesappvalueisforced(_:_:))*