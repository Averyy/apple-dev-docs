# CFPreferencesCopyKeyList(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Constructs and returns the list of all keys set in the specified domain.

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
func CFPreferencesCopyKeyList(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFArray?
```

#### Return Value

The list of keys. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `applicationID`: The ID of the application whose preferences to search. Takes the form of a Java package name,  .
- `userName`:   to search the current-user domain, otherwise   to search the any-user domain.
- `hostName`:   to search the current-host domain, otherwise   to search the any-host domain.

## See Also

- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](cfpreferencescopyappvalue(_:_:).md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](cfpreferencescopymultiple(_:_:_:_:).md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](cfpreferencescopyvalue(_:_:_:_:).md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](cfpreferencesgetappbooleanvalue(_:_:_:).md)
  Convenience function that directly obtains a Boolean preference value for the specified key.
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](cfpreferencesgetappintegervalue(_:_:_:).md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencescopykeylist(_:_:_:))*