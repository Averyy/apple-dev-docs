# CFPreferencesAppValueIsForced(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Determines whether or not a given key has been imposed on the user.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFPreferencesAppValueIsForced(_ key: CFString, _ applicationID: CFString) -> Bool
```

#### Return Value

`true` if value of the key cannot be changed by the user, otherwise `false`.

#### Discussion

In cases where machines and/or users are under some kind of management, you should use this function to determine whether or not to disable UI elements corresponding to those preference keys.

## Parameters

- `key`: The key you are querying.
- `applicationID`: The application’s ID, typically  . Do not pass   or  . Takes the form of a Java package name,  .

## See Also

- [func CFPreferencesCopyApplicationList(CFString, CFString) -> CFArray?](cfpreferencescopyapplicationlist(_:_:).md)
  Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesappvalueisforced(_:_:))*