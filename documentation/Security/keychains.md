# Keychains

**Framework**: Security

Create and manage entire keychains in macOS.

#### Overview

In iOS, apps have access to a single keychain (which logically encompasses the iCloud keychain). This keychain is automatically unlocked when the user unlocks the device and then locked when the device is locked. An app can access only its own keychain items, or those shared with a group to which the app belongs. It can’t manage the keychain container itself.

In macOS, however, the system supports an arbitrary number of keychains. You typically rely on the user to manage these with the Keychain Access app and work implicitly with the default keychain, much as you would in iOS. Nevertheless, the keychain services API does provide functions that you can use to manipulate keychains directly. For example, you can create and manage a keychain that is private to your app. On the other hand, robust access control mechanisms typically make this unnecessary for anything other than an app trying to replicate the keychain access utility.

## Topics

### Creation and Deletion
- [func SecKeychainCreate(UnsafePointer<CChar>, UInt32, UnsafeRawPointer?, Bool, SecAccess?, UnsafeMutablePointer<SecKeychain?>) -> OSStatus](seckeychaincreate(_:_:_:_:_:_:).md)
  Creates an empty keychain.
- [func SecKeychainDelete(SecKeychain?) -> OSStatus](seckeychaindelete(_:).md)
  Deletes one or more keychains from the default keychain search list, and removes the keychain itself if it is a file.
- [class SecKeychain](seckeychain.md)
  An opaque type that represents a keychain.
- [func SecKeychainGetTypeID() -> CFTypeID](seckeychaingettypeid().md)
  Returns the unique identifier of the opaque type to which a keychain object belongs.
### Locking and Unlocking
- [func SecKeychainLock(SecKeychain?) -> OSStatus](seckeychainlock(_:).md)
  Locks a keychain.
- [func SecKeychainLockAll() -> OSStatus](seckeychainlockall().md)
  Locks all keychains belonging to the current user.
- [func SecKeychainUnlock(SecKeychain?, UInt32, UnsafeRawPointer?, Bool) -> OSStatus](seckeychainunlock(_:_:_:_:).md)
  Unlocks a keychain.
### Settings
- [func SecKeychainSetSettings(SecKeychain?, UnsafePointer<SecKeychainSettings>) -> OSStatus](seckeychainsetsettings(_:_:).md)
  Changes the settings of a keychain.
- [func SecKeychainCopySettings(SecKeychain?, UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus](seckeychaincopysettings(_:_:).md)
  Obtains a keychain’s settings.
- [struct SecKeychainSettings](seckeychainsettings.md)
  A structure that contains information about keychain settings.
- [var SEC_KEYCHAIN_SETTINGS_VERS1: Int32](sec_keychain_settings_vers1.md)
  Defines the keychain settings version.
### Keychain Management
- [func SecKeychainGetVersion(UnsafeMutablePointer<UInt32>) -> OSStatus](seckeychaingetversion(_:).md)
  Determines the version of keychain services installed on the user’s system.
- [func SecKeychainOpen(UnsafePointer<CChar>, UnsafeMutablePointer<SecKeychain?>) -> OSStatus](seckeychainopen(_:_:).md)
  Opens a keychain.
- [func SecKeychainSetDefault(SecKeychain?) -> OSStatus](seckeychainsetdefault(_:).md)
  Sets the default keychain.
- [func SecKeychainCopyDefault(UnsafeMutablePointer<SecKeychain?>) -> OSStatus](seckeychaincopydefault(_:).md)
  Retrieves a pointer to the default keychain.
- [func SecKeychainGetPath(SecKeychain?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<CChar>) -> OSStatus](seckeychaingetpath(_:_:_:).md)
  Determines the path of a keychain.
- [func SecKeychainGetStatus(SecKeychain?, UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus](seckeychaingetstatus(_:_:).md)
  Retrieves status information of a keychain.
- [typealias SecKeychainStatus](seckeychainstatus.md)
  A value that defines the current status of a keychain.
- [SecKeychainStatus Values](seckeychainstatus-values.md)
  Valid values for the keychain status type.
### Search
- [func SecKeychainSetSearchList(CFArray) -> OSStatus](seckeychainsetsearchlist(_:).md)
  Specifies the list of keychains to use in the default keychain search list.
- [func SecKeychainCopySearchList(UnsafeMutablePointer<CFArray?>) -> OSStatus](seckeychaincopysearchlist(_:).md)
  Retrieves a keychain search list.
- [class SecKeychainSearch](seckeychainsearch.md)
  An opaque type that contains information about a keychain search.
### User Interaction
- [func SecKeychainSetUserInteractionAllowed(Bool) -> OSStatus](seckeychainsetuserinteractionallowed(_:).md)
  Enables or disables the user interface for keychain services functions that automatically display a user interface.
- [func SecKeychainGetUserInteractionAllowed(UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](seckeychaingetuserinteractionallowed(_:).md)
  Indicates whether keychain services functions that normally display a user interaction are allowed to do so.
### Callbacks
- [func SecKeychainAddCallback(SecKeychainCallback, SecKeychainEventMask, UnsafeMutableRawPointer?) -> OSStatus](seckeychainaddcallback(_:_:_:).md)
  Registers your keychain event callback function.
- [func SecKeychainRemoveCallback(SecKeychainCallback) -> OSStatus](seckeychainremovecallback(_:).md)
  Unregisters your keychain event callback function.
- [typealias SecKeychainCallback](seckeychaincallback.md)
  A customized callback function that keychain services call when a keychain event has occurred.
- [struct SecKeychainCallbackInfo](seckeychaincallbackinfo.md)
  Information about a keychain event that keychain services deliver to your app via a callback function.
- [enum SecKeychainEvent](seckeychainevent.md)
  The list of keychain events that can trigger a callback.
- [struct SecKeychainEventMask](seckeychaineventmask.md)
  Bit masks corresponding to the events that can trigger a keychain callback.
### Preference Domains
- [func SecKeychainGetPreferenceDomain(UnsafeMutablePointer<SecPreferencesDomain>) -> OSStatus](seckeychaingetpreferencedomain(_:).md)
  Gets the current keychain preference domain.
- [func SecKeychainSetPreferenceDomain(SecPreferencesDomain) -> OSStatus](seckeychainsetpreferencedomain(_:).md)
  Sets the keychain preference domain.
- [func SecKeychainCopyDomainDefault(SecPreferencesDomain, UnsafeMutablePointer<SecKeychain?>) -> OSStatus](seckeychaincopydomaindefault(_:_:).md)
  Retrieves the default keychain from a specified preference domain.
- [func SecKeychainSetDomainDefault(SecPreferencesDomain, SecKeychain?) -> OSStatus](seckeychainsetdomaindefault(_:_:).md)
  Sets the default keychain for a specified preference domain.
- [func SecKeychainCopyDomainSearchList(SecPreferencesDomain, UnsafeMutablePointer<CFArray?>) -> OSStatus](seckeychaincopydomainsearchlist(_:_:).md)
  Retrieves the keychain search list for a specified preference domain.
- [func SecKeychainSetDomainSearchList(SecPreferencesDomain, CFArray) -> OSStatus](seckeychainsetdomainsearchlist(_:_:).md)
  Sets the keychain search list for a specified preference domain.
- [enum SecPreferencesDomain](secpreferencesdomain.md)
  The keychain preference domains.
### Access
- [func SecKeychainSetAccess(SecKeychain?, SecAccess) -> OSStatus](seckeychainsetaccess(_:_:).md)
  Sets the application access for a keychain.
- [func SecKeychainCopyAccess(SecKeychain?, UnsafeMutablePointer<SecAccess?>) -> OSStatus](seckeychaincopyaccess(_:_:).md)
  Retrieves the application access of a keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/keychains)*