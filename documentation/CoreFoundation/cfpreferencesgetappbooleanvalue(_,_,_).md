# CFPreferencesGetAppBooleanValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Convenience function that directly obtains a Boolean preference value for the specified key.

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
func CFPreferencesGetAppBooleanValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> Bool
```

```c
extern Boolean CFPreferencesGetAppBooleanValue(CFStringRef key, CFStringRef applicationID, Boolean *keyExistsAndHasValidFormat);
```

#### Return Value

The preference data for the specified key and application, or if no value was located, `false`.

## Parameters

- `key`: The preference key whose value to obtain. The key must specify a preference whose value is of type `Boolean`.
- `applicationID`: The identifier of the application whose preferences are searched, typically [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](./kcfpreferencesanyapplication.md). Takes the form of a Java package name, such as `com.foosoft`.
- `keyExistsAndHasValidFormat`: On return, `true` if the preference value for the specified key was located and found to be of type `Boolean`, otherwise `false`.

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
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](./cfpreferencesgetappintegervalue%28_,_,_%29.md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappbooleanvalue(_:_:_:))*