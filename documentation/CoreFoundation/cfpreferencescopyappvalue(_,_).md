# CFPreferencesCopyAppValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Obtains a preference value for the specified key and application.

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
func CFPreferencesCopyAppValue(_ key: CFString, _ applicationID: CFString) -> CFPropertyList?
```

```c
extern CFPropertyListRefCFPreferencesCopyAppValue(CFStringRef key, CFStringRef applicationID);
```

## Return Value

The preference data for the specified key and application. If no value was located, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## Parameters

- `key`: The preference key whose value to obtain.
- `applicationID`: The identifier of the application whose preferences to search, typically [`kCFPreferencesCurrentApplication`](./kcfpreferencescurrentapplication.md). Do not pass `NULL` or [`kCFPreferencesAnyApplication`](./kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## See Also

### Getting Preference Values
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](./cfpreferencescopykeylist%28_,_,_%29.md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](./cfpreferencescopymultiple%28_,_,_,_%29.md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](./cfpreferencescopyvalue%28_,_,_,_%29.md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](./cfpreferencesgetappbooleanvalue%28_,_,_%29.md)
  Convenience function that directly obtains a Boolean preference value for the specified key.
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](./cfpreferencesgetappintegervalue%28_,_,_%29.md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopyappvalue(_:_:))*