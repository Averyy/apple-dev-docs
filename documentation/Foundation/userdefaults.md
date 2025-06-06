# UserDefaults

**Framework**: Foundation  
**Kind**: class

An interface to the user’s defaults database, where you store key-value pairs persistently across launches of your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UserDefaults
```

#### Overview

The [`UserDefaults`](userdefaults.md) class provides a programmatic interface for interacting with the defaults system. The defaults system allows an app to customize its behavior to match a user’s preferences. For example, you can allow users to specify their preferred units of measurement or media playback speed. Apps store these preferences by assigning values to a set of parameters in a user’s defaults database. The parameters are referred to as  because they’re commonly used to determine an app’s default state at startup or the way it acts by default.

At runtime, you use [`UserDefaults`](userdefaults.md) objects to read the defaults that your app uses from a user’s defaults database. [`UserDefaults`](userdefaults.md) caches the information to avoid having to open the user’s defaults database each time you need a default value. When you set a default value, it’s changed synchronously within your process, and asynchronously to persistent storage and other processes.

> ❗ **Important**:  Don’t try to access the preferences subsystem directly. Modifying preference property list files may result in loss of changes, delay of reflecting changes, and app crashes. To configure preferences, use the `defaults` command-line utility in macOS instead.

 Don’t try to access the preferences subsystem directly. Modifying preference property list files may result in loss of changes, delay of reflecting changes, and app crashes. To configure preferences, use the `defaults` command-line utility in macOS instead.

With the exception of managed devices in educational institutions, a user’s defaults are stored locally on a single device, and persisted for backup and restore. To synchronize preferences and other data across a user’s connected devices, use [`NSUbiquitousKeyValueStore`](nsubiquitouskeyvaluestore.md) instead.

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

 This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

##### Storing Default Objects

The [`UserDefaults`](userdefaults.md) class provides convenience methods for accessing common types such as floats, doubles, integers, Boolean values, and URLs. These methods are described in Setting Default Values.

A default object must be a property list—that is, an instance of (or for collections, a combination of instances of) [`NSData`](nsdata.md), [`NSString`](nsstring.md), [`NSNumber`](nsnumber.md), [`NSDate`](nsdate.md), [`NSArray`](nsarray.md), or [`NSDictionary`](nsdictionary.md). If you want to store any other type of object, you should typically archive it to create an instance of [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169).

Values returned from [`UserDefaults`](userdefaults.md) are immutable, even if you set a mutable object as the value. For example, if you set a mutable string as the value for “MyStringDefault”, the string you later retrieve using the [`string(forKey:)`](userdefaults/string(forkey:).md) method will be immutable. If you set a mutable string as a default value and later mutate the string, the default value won’t reflect the mutated string value unless you call [`set(_:forKey:)`](userdefaults/set(_:forkey:)-8ab6d.md) again.

For more details, see [`Preferences and Settings Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Introduction/Introduction.html#//apple_ref/doc/uid/10000059i).

##### Persisting File References

A file URL specifies a location in the file system. If you use the [`set(_:forKey:)`](userdefaults/set(_:forkey:)-2bqjt.md) method to store the location for a particular file and the user moves that file, your app may not be able to locate that file on next launch. To store a reference to a file by its file system identity, you can instead create [`NSURL`](nsurl.md) bookmark data using the [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md) method and persist it using the [`set(_:forKey:)`](userdefaults/set(_:forkey:)-8ab6d.md) method. You can then use the [`URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:`](nsurl/urlbyresolvingbookmarkdata:options:relativetourl:bookmarkdataisstale:error:.md) method to resolve the bookmark data stored in user defaults to a file URL.

##### Responding to Defaults Changes

You can use key-value observing to be notified of any updates to a particular default value. You can also register as an observer for [`didChangeNotification`](userdefaults/didchangenotification.md) on the [`default`](notificationcenter/default.md) notification center in order to be notified of all updates to a local defaults database.

For more details, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i) and [`Notification Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i).

##### Using Defaults in Managed Environments

If your app supports managed environments, you can use [`UserDefaults`](userdefaults.md) to determine which preferences are managed by an administrator for the benefit of the user. In a managed environment, such as a computer lab or classroom, an administrator or teacher can configure the systems by establishing a set of default preferences for users. If a preference is managed in this manner (as determined by the methods described in Accessing Managed Environment Keys), your app should prevent users from editing that preference by disabling or hiding controls.

For more details, see [`Mobile Device Management Protocol Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/1-Introduction/Introduction.html#//apple_ref/doc/uid/TP40017387).

An app running on a device managed by an educational institution can use the iCloud key-value store to share small amounts of data with other instances of itself on the user’s other devices. For example, a textbook app might store the current page number being read by the user so that other instances of the app can open to the same page when launched.

For more information, see [`Storing Preferences in iCloud`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/StoringPreferenceDatainiCloud/StoringPreferenceDatainiCloud.html#//apple_ref/doc/uid/10000059i-CH7) in [`Preferences and Settings Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Introduction/Introduction.html#//apple_ref/doc/uid/10000059i).

##### Sandbox Considerations

A sandboxed app cannot access or modify the preferences for any other app, with the following exceptions:

- App extensions on macOS and iOS
- Other apps in your application group on macOS

Adding a third-party app’s domain using the [`addSuite(named:)`](userdefaults/addsuite(named:).md) method doesn’t allow your app to access to that app’s preferences. Attempting to access or modify  another app’s preferences doesn’t result in an error; instead, macOS reads and writes files located within your app’s container, rather than the actual preference files for the other application.

##### Thread Safety

The [`UserDefaults`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/UserDefaults/Introduction/Intro.html#//apple_ref/doc/uid/DTS40008874-Intro) class is thread-safe.

## Topics

### Getting the Standard User Defaults Object
- [class var standard: UserDefaults](userdefaults/standard.md)
  Returns the shared defaults object.
### Creating User Defaults Objects
- [convenience init()](userdefaults/init.md)
  Creates a user defaults object initialized with the defaults for the app and current user.
- [init?(suiteName: String?)](userdefaults/init(suitename:).md)
  Creates a user defaults object initialized with the defaults for the specified database name.
### Getting Default Values
- [func object(forKey: String) -> Any?](userdefaults/object(forkey:).md)
  Returns the object associated with the specified key.
- [func url(forKey: String) -> URL?](userdefaults/url(forkey:).md)
  Returns the URL associated with the specified key.
- [func array(forKey: String) -> [Any]?](userdefaults/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](userdefaults/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [func string(forKey: String) -> String?](userdefaults/string(forkey:).md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](userdefaults/stringarray(forkey:).md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](userdefaults/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the float value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func dictionaryRepresentation() -> [String : Any]](userdefaults/dictionaryrepresentation.md)
  Returns a dictionary that contains a union of all key-value pairs in the domains in the search list.
### Setting Default Values
- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified default key.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified default key to the specified float value.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified default key to the double value.
- [func set(Int, forKey: String)](userdefaults/set(_:forkey:)-3v852.md)
  Sets the value of the specified default key to the specified integer value.
- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified default key to the specified Boolean value.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified default key to the specified URL.
### Removing Defaults
- [func removeObject(forKey: String)](userdefaults/removeobject(forkey:).md)
  Removes the value of the specified default key.
### Maintaining Suites
- [func addSuite(named: String)](userdefaults/addsuite(named:).md)
  Inserts the specified domain name into the receiver’s search list.
- [func removeSuite(named: String)](userdefaults/removesuite(named:).md)
  Removes the specified domain name from the receiver’s search list.
### Registering Defaults
- [func register(defaults: [String : Any])](userdefaults/register(defaults:).md)
  Adds the contents of the specified dictionary to the registration domain.
### Maintaining Persistent Domains
- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Returns a dictionary representation of the defaults for the specified domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Sets a dictionary for the specified persistent domain.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the contents of the specified persistent domain from the user’s defaults.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.
### Maintaining Volatile Domains
- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  The current volatile domain names.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Returns the dictionary for the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Sets the dictionary for the specified volatile domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the specified volatile domain from the user’s defaults.
### Accessing Managed Environment Keys
- [func objectIsForced(forKey: String) -> Bool](userdefaults/objectisforced(forkey:).md)
  Returns a Boolean value indicating whether the specified key is managed by an administrator.
- [func objectIsForced(forKey: String, inDomain: String) -> Bool](userdefaults/objectisforced(forkey:indomain:).md)
  Returns a Boolean value indicating whether the key in the specified domain is managed by an administrator.
### Domains
- [class let argumentDomain: String](userdefaults/argumentdomain.md)
  The domain consisting of defaults parsed from the application’s arguments. These are one or more pairs of the form  included in the command-line invocation of the application.
- [class let globalDomain: String](userdefaults/globaldomain.md)
  The domain consisting of defaults meant to be seen by all applications.
- [class let registrationDomain: String](userdefaults/registrationdomain.md)
  The domain consisting of a set of temporary defaults whose values can be set by the application to ensure that searches will always be successful.
### Notifications
- [class let didChangeNotification: NSNotification.Name](userdefaults/didchangenotification.md)
  Posted when user defaults are changed within the current process.
- [class let sizeLimitExceededNotification: NSNotification.Name](userdefaults/sizelimitexceedednotification.md)
  Posted when more data is stored in user defaults than is allowed.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
### Legacy
- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](userdefaults/synchronize.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [Language-Dependent Information Constants](language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults)*