# CFPreferencesCopyMultiple(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a dictionary containing preference values for multiple keys.

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
func CFPreferencesCopyMultiple(_ keysToFetch: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFDictionary
```

#### Return Value

A dictionary containing the preference values for the keys specified by `keysToFetch` for the specified domain. If no values were located, returns an empty dictionary. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## Parameters

- `keysToFetch`: An array of preference keys the values of which to obtain.
- `applicationID`: The ID of the application whose preferences are searched. Takes the form of a Java package name, such as  .
- `userName`:   to search the current-user domain, otherwise   to search the any-user domain.
- `hostName`:   to search the current-host domain, otherwise   to search the any-host domain.

## See Also

- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](cfpreferencescopyappvalue(_:_:).md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](cfpreferencescopykeylist(_:_:_:).md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](cfpreferencescopyvalue(_:_:_:_:).md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](cfpreferencesgetappbooleanvalue(_:_:_:).md)
  Convenience function that directly obtains a Boolean preference value for the specified key.
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](cfpreferencesgetappintegervalue(_:_:_:).md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopymultiple(_:_:_:_:))*