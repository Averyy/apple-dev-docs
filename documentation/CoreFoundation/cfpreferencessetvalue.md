# CFPreferencesSetValue(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds, modifies, or removes a preference value for the specified domain.

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
func CFPreferencesSetValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString)
```

#### Discussion

This function is the primitive set mechanism for the higher level preference function [`CFPreferencesSetAppValue(_:_:_:)`](cfpreferencessetappvalue(_:_:_:).md). Only the exact domain specified is modified. Do not use this function directly unless you have a specific need. All arguments except `value` must be non-`NULL`. Do not use arbitrary user and host names, instead pass the pre-defined constants.

You must call the [`CFPreferencesSynchronize(_:_:_:)`](cfpreferencessynchronize(_:_:_:).md) function in order for your changes to be saved to permanent storage. Note that you can only save preferences for “Any User” if you have root privileges (or Admin privileges prior to OS X v10.6).

## Parameters

- `key`: Preferences key for the value you wish to set.
- `value`: The value to set for   and application. Pass   to remove   from the domain.
- `applicationID`: The ID of the application whose preferences you wish to modify. Takes the form of a Java package name,  .
- `userName`:   to modify the current user’s preferences, otherwise   to modify the preferences of all users.
- `hostName`:   to modify the preferences of the current host, otherwise   to modify the preferences of all hosts.

## See Also

- [func CFPreferencesSetAppValue(CFString, CFPropertyList?, CFString)](cfpreferencessetappvalue(_:_:_:).md)
  Adds, modifies, or removes a preference.
- [func CFPreferencesSetMultiple(CFDictionary?, CFArray?, CFString, CFString, CFString)](cfpreferencessetmultiple(_:_:_:_:_:).md)
  Convenience function that allows you to set and remove multiple preference values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencessetvalue(_:_:_:_:_:))*