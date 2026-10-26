# SCDynamicStore

**Framework**: System Configuration  
**Role**: API Collection

#### Overview

The `SCDynamicStore` programming interface provides access to the key-value pairs in the dynamic store of a running system. The dynamic store contains, among other items, a copy of the configuration settings for the currently active set (which is sometimes refered to as the location) and information about the current network state.

The functions in the `SCDynamicStore` programming interface allow you to find key-value pairs, add or remove key-value pairs, add or change values, and request notifications. Note that these functions follow Core Foundation function-name conventions. A function that has “Create” or “Copy” in its name returns a reference you must release with the [`CFRelease`](../CoreFoundation/cfrelease.md) function.

To use these functions, you must first establish a dynamic store session using the [`SCDynamicStoreCreate(_:_:_:_:)`](./scdynamicstorecreate%28_,_,_,_%29.md) function. When you are finished with the session, use `CFRelease` to close it.

## Topics

### Creating a Dynamic Store Session
- [func SCDynamicStoreCreateWithOptions(CFAllocator?, CFString, CFDictionary?, SCDynamicStoreCallBack?, UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?](./scdynamicstorecreatewithoptions%28_,_,_,_,_%29.md)
  Creates a new session used to interact with the dynamic store maintained by the System Configuration server.
- [func SCDynamicStoreCreate(CFAllocator?, CFString, SCDynamicStoreCallBack?, UnsafeMutablePointer<SCDynamicStoreContext>?) -> SCDynamicStore?](./scdynamicstorecreate%28_,_,_,_%29.md)
  Creates a new session used to interact with the dynamic store maintained by the System Configuration server.
### Adding or Updating Keys and Values
- [func SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList) -> Bool](./scdynamicstoreaddtemporaryvalue%28_,_,_%29.md)
  Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreAddValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](./scdynamicstoreaddvalue%28_,_,_%29.md)
  Adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetMultiple(SCDynamicStore?, CFDictionary?, CFArray?, CFArray?) -> Bool](./scdynamicstoresetmultiple%28_,_,_,_%29.md)
  Updates multiple values in the dynamic store.
- [func SCDynamicStoreSetValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](./scdynamicstoresetvalue%28_,_,_%29.md)
  Adds or replaces a value in the dynamic store for the specified key.
### Getting Keys and Values
- [func SCDynamicStoreCopyKeyList(SCDynamicStore?, CFString) -> CFArray?](./scdynamicstorecopykeylist%28_,_%29.md)
  Returns the keys that represent the current dynamic store entries that match the specified pattern.
- [func SCDynamicStoreCopyMultiple(SCDynamicStore?, CFArray?, CFArray?) -> CFDictionary?](./scdynamicstorecopymultiple%28_,_,_%29.md)
  Returns the key-value pairs that match the specified keys and key patterns.
- [func SCDynamicStoreCopyNotifiedKeys(SCDynamicStore) -> CFArray?](./scdynamicstorecopynotifiedkeys%28_%29.md)
  Returns the keys that have changed since the last call to this function.
- [func SCDynamicStoreCopyValue(SCDynamicStore?, CFString) -> CFPropertyList?](./scdynamicstorecopyvalue%28_,_%29.md)
  Returns the value associated with the specified key.
### Monitoring Keys and Values
- [func SCDynamicStoreNotifyValue(SCDynamicStore?, CFString) -> Bool](./scdynamicstorenotifyvalue%28_,_%29.md)
  Causes a notification to be delivered for the specified key in the dynamic store.
- [func SCDynamicStoreSetNotificationKeys(SCDynamicStore, CFArray?, CFArray?) -> Bool](./scdynamicstoresetnotificationkeys%28_,_,_%29.md)
  Specifies a set of keys and key patterns that should be monitored for changes.
- [func SCDynamicStoreSetDispatchQueue(SCDynamicStore, dispatch_queue_t?) -> Bool](./scdynamicstoresetdispatchqueue%28_,_%29.md)
  Initiates notifications for the notification keys, using the specified dispatch queue for the callback.
### Removing Keys and Values
- [func SCDynamicStoreRemoveValue(SCDynamicStore?, CFString) -> Bool](./scdynamicstoreremovevalue%28_,_%29.md)
  Removes the value of the specified key from the dynamic store.
### Creating a Run Loop Source
- [func SCDynamicStoreCreateRunLoopSource(CFAllocator?, SCDynamicStore, CFIndex) -> CFRunLoopSource?](./scdynamicstorecreaterunloopsource%28_,_,_%29.md)
  Creates a run loop source object that can be added to the application’s run loop.
### Getting Information About the Dynamic Store
- [func SCDynamicStoreGetTypeID() -> CFTypeID](./scdynamicstoregettypeid%28%29.md)
  Returns the type identifier of all `SCDynamicStore` instances.
### Data Types
- [typealias SCDynamicStoreCallBack](./scdynamicstorecallback.md)
  Callback used when notification of changes made to the dynamic store is delivered.
- [struct SCDynamicStoreContext](./scdynamicstorecontext.md)
  Structure containing user-specified data and callbacks for a dynamic store session.
- [class SCDynamicStore](./scdynamicstore.md)
  The handle to an open dynamic store session with the system configuration daemon.
### Constants
- [Dynamic Store Options Keys](./dynamic-store-options-keys.md)
  Keys that indicate the options for a dynamic store session.

## See Also

### Reference
- [SCDynamicStoreCopySpecific](./scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](./scdynamicstorekey.md)
- [SCNetwork](./scnetwork.md)
- [SCNetworkConfiguration](./scnetworkconfiguration.md)
- [SCNetworkConnection](./scnetworkconnection-g7e.md)
- [SCNetworkReachability](./scnetworkreachability-g7d.md)
- [SCPreferences](./scpreferences-ft8.md)
- [SCPreferencesPath](./scpreferencespath.md)
- [SCPreferencesSetSpecific](./scpreferencessetspecific.md)
- [SCSchemaDefinitions](./scschemadefinitions.md)
- [System Configuration](./system-configuration.md)
- [SystemConfiguration Enumerations](./systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](./systemconfiguration-constants.md)
- [SystemConfiguration Functions](./systemconfiguration-functions.md)
- [SystemConfiguration Data Types](./systemconfiguration-data-types.md)
- [DHCPClientPreferences](./dhcpclientpreferences.md)
- [SCDynamicStoreCopyDHCPInfo](./scdynamicstorecopydhcpinfo-apicollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstore-gb2)*