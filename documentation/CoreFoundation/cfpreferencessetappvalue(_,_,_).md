# CFPreferencesSetAppValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds, modifies, or removes a preference.

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
func CFPreferencesSetAppValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString)
```

```c
extern void CFPreferencesSetAppValue(CFStringRef key, CFPropertyListRef value, CFStringRef applicationID);
```

## Discussion

New preference values are stored in the standard application preference location, `~/Library/Preferences/`. When called with [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md), modifications are performed in the preference domain “Current User, Current Application, Any Host.” If you need to create preferences in some other domain, use the low-level function [`CFPreferencesSetValue(_:_:_:_:_:)`](./cfpreferencessetvalue%28_,_,_,_,_%29.md).

You must call the [`CFPreferencesAppSynchronize(_:)`](./cfpreferencesappsynchronize%28_%29.md) function in order for your changes to be saved to permanent storage.

## Parameters

- `key`: The preference key whose value you wish to set.
- `value`: The value to set for the specified `key` and application. Pass `NULL` to remove the specified key from the application’s preferences.
- `applicationID`: The ID of the application whose preferences you wish to create or modify, typically [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](./kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## See Also

### Setting Preference Values
- [func CFPreferencesSetMultiple(CFDictionary?, CFArray?, CFString, CFString, CFString)](./cfpreferencessetmultiple%28_,_,_,_,_%29.md)
  Convenience function that allows you to set and remove multiple preference values.
- [func CFPreferencesSetValue(CFString, CFPropertyList?, CFString, CFString, CFString)](./cfpreferencessetvalue%28_,_,_,_,_%29.md)
  Adds, modifies, or removes a preference value for the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencessetappvalue(_:_:_:))*