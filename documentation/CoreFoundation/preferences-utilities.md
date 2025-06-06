# Preferences Utilities

**Framework**: Core Foundation

#### Overview

Several functions return a preference value as a Core Foundation property list object.

You can use the function [`CFGetTypeID(_:)`](cfgettypeid(_:).md) to determine the value’s type. For more information about property lists, see [`Property List Programming Topics for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i).

##### Overview

Core Foundation provides a simple, standard way to manage user (and application) preferences. Core Foundation stores preferences as key-value pairs that are assigned a scope using a combination of user name, application ID, and host (computer) names. This makes it possible to save and retrieve preferences that apply to different classes of users. Core Foundation preferences is useful to all applications that support user preferences. Note that modification of some preferences domains (those not belonging to the “Current User”) requires root privileges (or Admin privileges prior to OS X v10.6)—see [`Authorization Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995) for information on how to gain suitable privileges.

Unlike some other Core Foundation types, CFPreferences is not toll-free bridged to its corresponding Cocoa Foundation framework class (`NSUserDefaults`). CFPreferences is thread-safe.

## Topics

### Getting Preference Values
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
- [func CFPreferencesGetAppIntegerValue(CFString, CFString, UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex](cfpreferencesgetappintegervalue(_:_:_:).md)
  Convenience function that directly obtains an integer preference value for the specified key.
### Setting Preference Values
- [func CFPreferencesSetAppValue(CFString, CFPropertyList?, CFString)](cfpreferencessetappvalue(_:_:_:).md)
  Adds, modifies, or removes a preference.
- [func CFPreferencesSetMultiple(CFDictionary?, CFArray?, CFString, CFString, CFString)](cfpreferencessetmultiple(_:_:_:_:_:).md)
  Convenience function that allows you to set and remove multiple preference values.
- [func CFPreferencesSetValue(CFString, CFPropertyList?, CFString, CFString, CFString)](cfpreferencessetvalue(_:_:_:_:_:).md)
  Adds, modifies, or removes a preference value for the specified domain.
### Synchronizing Preferences
- [func CFPreferencesAppSynchronize(CFString) -> Bool](cfpreferencesappsynchronize(_:).md)
  Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.
- [func CFPreferencesSynchronize(CFString, CFString, CFString) -> Bool](cfpreferencessynchronize(_:_:_:).md)
  For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.
### Adding and Removing Suite Preferences
- [func CFPreferencesAddSuitePreferencesToApp(CFString, CFString)](cfpreferencesaddsuitepreferencestoapp(_:_:).md)
  Adds suite preferences to an application’s preference search chain.
- [func CFPreferencesRemoveSuitePreferencesFromApp(CFString, CFString)](cfpreferencesremovesuitepreferencesfromapp(_:_:).md)
  Removes suite preferences from an application’s search chain.
### Miscellaneous Functions
- [func CFPreferencesAppValueIsForced(CFString, CFString) -> Bool](cfpreferencesappvalueisforced(_:_:).md)
  Determines whether or not a given key has been imposed on the user.
- [func CFPreferencesCopyApplicationList(CFString, CFString) -> CFArray?](cfpreferencescopyapplicationlist(_:_:).md)
  Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.
### Constants
- [Application, Host, and User Keys](application-host-and-user-keys.md)
  Keys used to specify the common preference domains.

## See Also

- [Preferences Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/CFPreferences.html#//apple_ref/doc/uid/10000129i)
- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/preferences-utilities)*