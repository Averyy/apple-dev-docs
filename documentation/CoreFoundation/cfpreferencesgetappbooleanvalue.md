# CFPreferencesGetAppBooleanValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Convenience function that directly obtains a Boolean preference value for the specified key.

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
func CFPreferencesGetAppBooleanValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> Bool
```

#### Return Value

The preference data for the specified key and application, or if no value was located, `false`.

## Parameters

- `key`: The preference key whose value to obtain. The key must specify a preference whose value is of type  .
- `applicationID`: The identifier of the application whose preferences are searched, typically  . Do not pass   or  . Takes the form of a Java package name, such as  .
- `keyExistsAndHasValidFormat`: On return,   if the preference value for the specified key was located and found to be of type  , otherwise  .

## See Also

- [func CFPreferencesCopyAppValue(CFString, CFString) -> CFPropertyList?](cfpreferencescopyappvalue(_:_:).md)
  Obtains a preference value for the specified key and application.
- [func CFPreferencesCopyKeyList(CFString, CFString, CFString) -> CFArray?](cfpreferencescopykeylist(_:_:_:).md)
  Constructs and returns the list of all keys set in the specified domain.
- [func CFPreferencesCopyMultiple(CFArray?, CFString, CFString, CFString) -> CFDictionary](cfpreferencescopymultiple(_:_:_:_:).md)
  Returns a dictionary containing preference values for multiple keys.
- [func CFPreferencesCopyValue(CFString, CFString, CFString, CFString) -> CFPropertyList?](cfpreferencescopyvalue(_:_:_:_:).md)
  Returns a preference value for a given domain.
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](cfpreferencesgetappintegervalue(_:_:_:).md)
  Convenience function that directly obtains an integer preference value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappbooleanvalue(_:_:_:))*