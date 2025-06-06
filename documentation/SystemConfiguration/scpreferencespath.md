# SCPreferencesPath

**Framework**: System Configuration

#### Overview

The `SCPreferencesPath` programming interface allows an application to load and store XML configuration data in a controlled manner and provide the necessary notifications to other applications that need to be aware of configuration changes.

The functions in this programming interface view the data as a collection of dictionaries of key-value pairs and an associated path name. The root path (”/”) identifies the top-level dictionary. Additional path components specify the keys for subdictionaries.

For example, the following dictionary can be accessed via two paths. The root path (”/”) returns a dictionary with all keys and values. The path “/path1” returns only the dictionary with the “key3” and “key4” properties.

```objc
<dict>
   <key>key1</key>
   <string>val1</string>
   <key>key2</key>
   <string>val2</string>
   <key>path1</key>
   <dict>
      <key>key3</key>
      <string>val3</string>
      <key>key4</key>
      <string>val4</string>
   </dict>
</dict>
```

Each dictionary can also include the `kSCResvLink` (”__LINK__”) key. The value associated with this key is interpreted as a link to another path. If this key is present, a call to the [`SCPreferencesPathGetValue(_:_:)`](scpreferencespathgetvalue(_:_:).md) function returns the dictionary specified by the link.

## Topics

### Creating a New Path
- [func SCPreferencesPathCreateUniqueChild(SCPreferences, CFString) -> CFString?](scpreferencespathcreateuniquechild(_:_:).md)
  Creates a new path component rooted at the specified path in the dictionary hierarchy.
### Associating Information with a Path
- [func SCPreferencesPathSetValue(SCPreferences, CFString, CFDictionary) -> Bool](scpreferencespathsetvalue(_:_:_:).md)
  Associates the specified dictionary with the specified path.
- [func SCPreferencesPathSetLink(SCPreferences, CFString, CFString) -> Bool](scpreferencespathsetlink(_:_:_:).md)
  Associates a link to a second dictionary at the specified path.
### Getting or Removing Information Associated with a Path
- [func SCPreferencesPathGetValue(SCPreferences, CFString) -> CFDictionary?](scpreferencespathgetvalue(_:_:).md)
  Returns the dictionary associated with the specified path.
- [func SCPreferencesPathGetLink(SCPreferences, CFString) -> CFString?](scpreferencespathgetlink(_:_:).md)
  Returns the link associated with the specified path.
- [func SCPreferencesPathRemoveValue(SCPreferences, CFString) -> Bool](scpreferencespathremovevalue(_:_:).md)
  Removes the data associated with the specified path.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConfiguration](scnetworkconfiguration.md)
- [SCNetworkConnection](scnetworkconnection-g7e.md)
- [SCNetworkReachability](scnetworkreachability-g7d.md)
- [SCPreferences](scpreferences-ft8.md)
- [SCPreferencesSetSpecific](scpreferencessetspecific.md)
- [SCSchemaDefinitions](scschemadefinitions.md)
- [System Configuration](system-configuration.md)
- [SystemConfiguration Enumerations](systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](systemconfiguration-constants.md)
- [SystemConfiguration Functions](systemconfiguration-functions.md)
- [SystemConfiguration Data Types](systemconfiguration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencespath)*