# CFPreferencesSetMultiple(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Convenience function that allows you to set and remove multiple preference values.

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
func CFPreferencesSetMultiple(_ keysToSet: CFDictionary?, _ keysToRemove: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString)
```

#### Discussion

Behavior is undefined if a key is in both `keysToSet` and `keysToRemove`

## Parameters

- `keysToSet`: A dictionary containing the key/value pairs for the preferences  to set.
- `keysToRemove`: An array containing a list of keys to remove.
- `applicationID`: The ID of the application whose preferences you wish to modify. Takes the form of a Java package name,  .
- `userName`:   to modify the current user’s preferences, otherwise   to modify the preferences of all users.
- `hostName`:   to modify the preferences of the current host, otherwise   to modify the preferences of all hosts.

## See Also

- [func CFPreferencesSetAppValue(CFString, CFPropertyList?, CFString)](cfpreferencessetappvalue(_:_:_:).md)
  Adds, modifies, or removes a preference.
- [func CFPreferencesSetValue(CFString, CFPropertyList?, CFString, CFString, CFString)](cfpreferencessetvalue(_:_:_:_:_:).md)
  Adds, modifies, or removes a preference value for the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencessetmultiple(_:_:_:_:_:))*