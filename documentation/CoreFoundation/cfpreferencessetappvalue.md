# CFPreferencesSetAppValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds, modifies, or removes a preference.

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
func CFPreferencesSetAppValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString)
```

#### Discussion

New preference values are stored in the standard application preference location, `~/Library/Preferences/`. When called with [`kCFPreferencesCurrentApplication`](kcfpreferencescurrentapplication.md), modifications are performed in the preference domain “Current User, Current Application, Any Host.” If you need to create preferences in some other domain, use the low-level function [`CFPreferencesSetValue(_:_:_:_:_:)`](cfpreferencessetvalue(_:_:_:_:_:).md).

You must call the [`CFPreferencesAppSynchronize(_:)`](cfpreferencesappsynchronize(_:).md) function in order for your changes to be saved to permanent storage.

## Parameters

- `key`: The preference key whose value you wish to set.
- `value`: The value to set for the specified   and application. Pass   to remove the specified key from the application’s preferences.
- `applicationID`: The ID of the application whose preferences you wish to create or modify, typically  . Do not pass   or  . Takes the form of a Java package name,  .

## See Also

- [func CFPreferencesSetMultiple(CFDictionary?, CFArray?, CFString, CFString, CFString)](cfpreferencessetmultiple(_:_:_:_:_:).md)
  Convenience function that allows you to set and remove multiple preference values.
- [func CFPreferencesSetValue(CFString, CFPropertyList?, CFString, CFString, CFString)](cfpreferencessetvalue(_:_:_:_:_:).md)
  Adds, modifies, or removes a preference value for the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencessetappvalue(_:_:_:))*