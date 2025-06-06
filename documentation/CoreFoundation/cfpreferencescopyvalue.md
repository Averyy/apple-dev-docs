# CFPreferencesCopyValue(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a preference value for a given domain.

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
func CFPreferencesCopyValue(_ key: CFString, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFPropertyList?
```

#### Return Value

The preference data for the specified domain. If the no value was located, returns `NULL`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function is the primitive get mechanism for the higher level preference function [`CFPreferencesCopyAppValue(_:_:)`](cfpreferencescopyappvalue(_:_:).md) Unlike the high-level function, [`CFPreferencesCopyValue(_:_:_:_:)`](cfpreferencescopyvalue(_:_:_:_:).md) searches only the exact domain specified. Do not use this function directly unless you have a need. All arguments must be non-`NULL`. Do not use arbitrary user and host names, instead pass the pre-defined domain qualifier constants.

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## Parameters

- `key`: Preferences key for the value to obtain.
- `applicationID`: The ID of the application whose preferences are searched. Takes the form of a Java package name, such as  .
- `userName`:   if to search the current-user domain, otherwise   to search the any-user domain.
- `hostName`:   if to search the current-host domain, otherwise   to search the any-host domain.

## See Also

- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](cfpreferencescopyappvalue(_:_:).md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](cfpreferencescopykeylist(_:_:_:).md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](cfpreferencescopymultiple(_:_:_:_:).md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](cfpreferencesgetappbooleanvalue(_:_:_:).md)
  Convenience function that directly obtains a Boolean preference value for the specified key.
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](cfpreferencesgetappintegervalue(_:_:_:).md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopyvalue(_:_:_:_:))*