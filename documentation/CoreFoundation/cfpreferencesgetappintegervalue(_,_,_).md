# CFPreferencesGetAppIntegerValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Convenience function that directly obtains an integer preference value for the specified key.

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
func CFPreferencesGetAppIntegerValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex
```

```c
extern CFIndex CFPreferencesGetAppIntegerValue(CFStringRef key, CFStringRef applicationID, Boolean *keyExistsAndHasValidFormat);
```

## Return Value

The preference data for the specified key and application. If no value was located, `0` is returned.

## Parameters

- `key`: The preference key whose value you wish to obtain. The key must specify a preference whose value is of type `int`.
- `applicationID`: The identifier of the application whose preferences you wish to search, typically [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](./kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.
- `keyExistsAndHasValidFormat`: On return, indicates whether the preference value for the specified key was located and found to be of type `int`.

## See Also

### Getting Preference Values
- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](./cfpreferencescopyappvalue%28_,_%29.md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](./cfpreferencescopykeylist%28_,_,_%29.md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](./cfpreferencescopymultiple%28_,_,_,_%29.md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](./cfpreferencescopyvalue%28_,_,_,_%29.md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](./cfpreferencesgetappbooleanvalue%28_,_,_%29.md)
  Convenience function that directly obtains a Boolean preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappintegervalue(_:_:_:))*