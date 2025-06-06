# SCPreferences

**Framework**: System Configuration

#### Overview

The `SCPreferences` programming interface allows an application to load and store XML configuration data in a controlled manner and provide the necessary notifications to other applications that need to be aware of configuration changes.

To access configuration preferences, you must first establish a preferences session using the [`SCPreferencesCreate(_:_:_:)`](scpreferencescreate(_:_:_:).md) function. To identify a specific set of preferences to access, you pass a value in the prefsID parameter. A `NULL` value indicates that the default system preferences are to be accessed. A string that starts with a leading “/” character specifies the absolute path to the file containing the preferences to be accessed. A string that does not start with a leading “/” character specifies a file relative to the default system preferences directory.

When you are finished with the preferences session, use the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to release it.

## Topics

### Creating a Preferences Session
- [func SCPreferencesCreate(CFAllocator?, CFString, CFString?) -> SCPreferences?](scpreferencescreate(_:_:_:).md)
  Initiates access to the per-system set of configuration preferences.
- [func SCPreferencesCreateWithAuthorization(CFAllocator?, CFString, CFString?, AuthorizationRef?) -> SCPreferences?](scpreferencescreatewithauthorization(_:_:_:_:).md)
  Initiates access to the per-system set of configuration preferences with the specified authorization.
### Getting Information About a Preferences Session
- [func SCPreferencesGetTypeID() -> CFTypeID](scpreferencesgettypeid().md)
  Returns the type identifier of all `SCPreferences` instances.
- [func SCPreferencesCopyKeyList(SCPreferences) -> CFArray?](scpreferencescopykeylist(_:).md)
  Returns the currently defined preference keys.
- [func SCPreferencesGetSignature(SCPreferences) -> CFData?](scpreferencesgetsignature(_:).md)
  Returns a value that can be used to determine if the saved configuration preferences have changed.
### Adding, Getting, and Removing Values
- [func SCPreferencesAddValue(SCPreferences, CFString, CFPropertyList) -> Bool](scpreferencesaddvalue(_:_:_:).md)
  Associates the specified value with the specified preference key.
- [func SCPreferencesGetValue(SCPreferences, CFString) -> CFPropertyList?](scpreferencesgetvalue(_:_:).md)
  Retrieves the value associated with the specified preference key.
- [func SCPreferencesSetValue(SCPreferences, CFString, CFPropertyList) -> Bool](scpreferencessetvalue(_:_:_:).md)
  Updates the data associated with the specified preference key with the specified value.
- [func SCPreferencesRemoveValue(SCPreferences, CFString) -> Bool](scpreferencesremovevalue(_:_:).md)
  Removes the data associated with the specified preference key.
### Applying and Committing Changes
- [func SCPreferencesApplyChanges(SCPreferences) -> Bool](scpreferencesapplychanges(_:).md)
  Requests that the currently stored configuration preferences be applied to the active configuration.
- [func SCPreferencesCommitChanges(SCPreferences) -> Bool](scpreferencescommitchanges(_:).md)
  Commits changes made to the configuration preferences to persistent storage.
- [func SCPreferencesSynchronize(SCPreferences)](scpreferencessynchronize(_:).md)
  Synchronizes accessed preferences with committed changes.
### Managing Notifications and Callbacks
- [func SCPreferencesSetCallback(SCPreferences, SCPreferencesCallBack?, UnsafeMutablePointer<SCPreferencesContext>?) -> Bool](scpreferencessetcallback(_:_:_:).md)
  Assigns the specified callback to the specified preferences session.
- [func SCPreferencesScheduleWithRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesschedulewithrunloop(_:_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified run loop and mode.
- [func SCPreferencesUnscheduleFromRunLoop(SCPreferences, CFRunLoop, CFString) -> Bool](scpreferencesunschedulefromrunloop(_:_:_:).md)
  Unschedules commit and apply notifications for the specified preferences session from the specified run loop and mode.
- [func SCPreferencesSetDispatchQueue(SCPreferences, dispatch_queue_t?) -> Bool](scpreferencessetdispatchqueue(_:_:).md)
  Schedules commit and apply notifications for the specified preferences session using the specified dispatch queue.
### Managing Access to a Preferences Session
- [func SCPreferencesLock(SCPreferences, Bool) -> Bool](scpreferenceslock(_:_:).md)
  Locks access to the configuration preferences.
- [func SCPreferencesUnlock(SCPreferences) -> Bool](scpreferencesunlock(_:).md)
  Releases exclusive access to the configuration preferences.
### Data Types
- [class SCPreferences](scpreferences.md)
  The handle to an open preferences session for accessing system configuration preferences.
- [struct SCPreferencesContext](scpreferencescontext.md)
  A structure containing user-specified data and callbacks for accessing system configuration preferences.
- [typealias SCPreferencesCallBack](scpreferencescallback.md)
  Type of the callback function used when the preferences have been updated or applied.
### Constants
- [struct SCPreferencesNotification](scpreferencesnotification.md)
  The type of notification (used with the [`SCPreferencesCallBack`](scpreferencescallback.md) callback).

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConfiguration](scnetworkconfiguration.md)
- [SCNetworkConnection](scnetworkconnection-g7e.md)
- [SCNetworkReachability](scnetworkreachability-g7d.md)
- [SCPreferencesPath](scpreferencespath.md)
- [SCPreferencesSetSpecific](scpreferencessetspecific.md)
- [SCSchemaDefinitions](scschemadefinitions.md)
- [System Configuration](system-configuration.md)
- [SystemConfiguration Enumerations](systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](systemconfiguration-constants.md)
- [SystemConfiguration Functions](systemconfiguration-functions.md)
- [SystemConfiguration Data Types](systemconfiguration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferences-ft8)*