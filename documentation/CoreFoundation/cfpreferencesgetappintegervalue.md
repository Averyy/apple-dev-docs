# CFPreferencesGetAppIntegerValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Convenience function that directly obtains an integer preference value for the specified key.

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
func CFPreferencesGetAppIntegerValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex
```

#### Return Value

The preference data for the specified key and application. If no value was located, `0` is returned.

## Parameters

- `key`: The preference key whose value you wish to obtain. The key must specify a preference whose value is of type  .
- `applicationID`: The identifier of the application whose preferences you wish to search, typically  . Do not pass   or  . Takes the form of a Java package name,  .
- `keyExistsAndHasValidFormat`: On return, indicates whether the preference value for the specified key was located and found to be of type  .

## See Also

- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](cfpreferencescopyappvalue(_:_:).md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](cfpreferencescopykeylist(_:_:_:).md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](cfpreferencescopymultiple(_:_:_:_:).md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](cfpreferencescopyvalue(_:_:_:_:).md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppBooleanValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> Bool](cfpreferencesgetappbooleanvalue(_:_:_:).md)
  Convenience function that directly obtains a Boolean preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappintegervalue(_:_:_:))*