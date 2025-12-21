# UserDefaults

**Framework**: Foundation  
**Kind**: class

An interface to the user’s defaults database, which stores system-wide and app-specific settings.

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

## Mentions

- [Accessing settings from your code](accessing-settings-from-your-code.md)
- [Adding a settings interface to your app](adding-a-settings-interface-to-your-app.md)
- [Using the file system effectively](using-the-file-system-effectively.md)

#### Overview

A `UserDefaults` object provides access to the defaults system, which is a persistent store for app-specific and system-wide settings. You use this system to store nonsensitive information, such as app-specific configuration details. The system also stores configuration details that apply to all apps, such as the current language settings for the device. In your code, you check values from this system and use them to dynamically alter your app’s appearance or behavior. The term  refers to the fact that the stored data determines the default startup state and behavior.

> ❗ **Important**: Don’t store personal or sensitive information as settings. The defaults system stores information on disk in an unencrypted format. Store personal or sensitive information in the person’s Keychain instead.

To access the defaults system, obtain a `UserDefaults` object and call its methods to read and write values. The [`standard`](userdefaults/standard.md) object is a shared object you use to read and write your app’s standard settings. You can also create unique `UserDefaults` objects to manage specific sets of settings. For example, you can create a `UserDefaults` object that reads and writes settings your app shares with an app extension. Don’t subclass `UserDefaults`.

Each item you store in a defaults object consists of a key-value pair, where each key is a string that you use to locate the item and each value is a data object. The defaults database supports the same value types found in property list files, including types like [`Int`](https://developer.apple.com/documentation/Swift/Int), [`Float`](https://developer.apple.com/documentation/Swift/Float), [`Double`](https://developer.apple.com/documentation/Swift/Double), [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`String`](https://developer.apple.com/documentation/Swift/String), [`URL`](url.md), [`NSNumber`](NSNumber.md), [`Date`](date.md), [`Array`](https://developer.apple.com/documentation/Swift/Array), and [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary). To include other types of objects in the defaults database, archive them to a [`Data`](data.md) object first and store that object instead. Prefer simple types over custom objects whenever possible.

With the exception of managed devices in educational institutions, the system stores defaults locally on the current device. When you write values to a `UserDefaults` object, the object updates its in-memory version of that information right away, and writes the value to disk asynchronously.  When someone backs up their device, the system includes any persistent defaults databases in the backup data. Because the data is device-specific, you don’t use the defaults system to share data between devices. To share data between someone’s devices, use the [`NSUbiquitousKeyValueStore`](nsubiquitouskeyvaluestore.md) instead.

> ⚠️ **Warning**: Don’t access the files of the defaults database directly from the file system. Modifying one of the underlying files directly may cause data loss, a delay in changes being available, or an app crash. In macOS, use the `defaults` command-line utility to safely view or modify the defaults database outside of your app.

While your app is running, the defaults system generates notifications to let you know when values change. To observe changes to individual settings, add a [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift) to your `UserDefaults` object, using key names to build the path to the setting you want. To observe changes for all settings, register for a [`UserDefaults.DidChangeMessage`](userdefaults/didchangemessage.md) or [`didChangeNotification`](userdefaults/didchangenotification.md) with your `UserDefaults` object.

The `UserDefaults` type is thread-safe, and you can use the same object in multiple threads or tasks simultaneously.

> ❗ **Important**: This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

##### Domains and Settings Search Paths

To integrate settings from different sources, the defaults system organizes them into domains. An app defines its own custom settings, but the system defines settings that apply to all apps. Similarly, you might choose to override a specific setting temporarily to test one of your app’s features. The defaults system provides domains for each of these cases along with several others.

When you request the value of a setting, the `UserDefaults` object searches its domains in a specific order until it finds the value you want. The following table lists the key domains that the defaults system supports and their search order. Some domains might not be present for all apps. For example, the managed domain is present only on administrator-managed devices.

| Domain | Type | Description |
| --- | --- | --- |
| Managed | persistent | This domain contains settings that an administrator provided for a managed device. The system saves these values persistently on the current device. |
| [`argumentDomain`](UserDefaults/argumentDomain.md) | volatile | This domain contains the settings you specified when launching your app from the command-line or Xcode. These keys represent temporary overrides of settings, and the system discards them after the app quits. |
| Educational managed | persistent | For managed devices in an educational institution, this domain contains any settings saved to the iCloud key-value store for that institution. The system saves these settings persistently on a server, not on the device. |
| App | persistent | This domain contains the settings your app saves, either programmatically or using its settings UI. Each `UserDefaults` object writes settings to this group, associating them with the app itself or the app group you used to initialize the object. The system saves these settings persistently on the current device. |
| Suite | persistent | This domain contains custom settings from an app group or other app you specify at runtime. This domain is absent by default, but you can add a suite using the [`addSuite(named:)`](userdefaults/addsuite(named:).md) method. The system saves these settings persistently on the current device. |
| [`globalDomain`](UserDefaults/globalDomain.md) | persistent | This domain contains keys present for all apps on the system. The system provides the keys for this domain, and apps can’t write to it. The system saves these settings persistently on the current device. |
| [`registrationDomain`](UserDefaults/registrationDomain.md) | volatile | This domain contains system-provided default values and the default values you register for your app at launch time. Registering a set of default values prevents your code from receiving `nil` values when requesting a setting. The system discards these values when your app quits, so you must register them each time your app launches. |

The system stores data for most persistent domains on the current device, and doesn’t share that data with other devices. To share settings among all of a person’s devices, save them using an [`NSUbiquitousKeyValueStore`](nsubiquitouskeyvaluestore.md) object instead.

##### Settings in Managed Environments

If your app supports managed environments, an administrator might configure any managed devices with a default set of settings. For example, in a computer lab or classrom environment, a teacher might set default settings that the lessons require. Apps can’t write to managed domains, so if your app encounters a managed setting, disable or hide any controls that someone might use to change that setting’s value. To determine if a setting is managed, call the [`objectIsForced(forKey:)`](userdefaults/objectisforced(forkey:).md) or [`objectIsForced(forKey:inDomain:)`](userdefaults/objectisforced(forkey:indomain:).md) method of your `UserDefaults` object.

An app running on a managed device can use [`NSUbiquitousKeyValueStore`](nsubiquitouskeyvaluestore.md) to share small amounts of data with the person’s other devices. Use this store for data that your app can safely share with other instances of itself. For example, a textbook app might save the current page number so that the person can continue reading from the same place on any of their devices.

For more details about managing devices, see [`Device Management`](https://developer.apple.com/documentation/DeviceManagement).

##### Sandbox Considerations

A sandboxed app cannot access or modify the settings of another app or process, with the following exceptions:

- An app can modify settings for one of its app extensions.
- An app can modify settings for an app group to which it belongs.

If you use the [`addSuite(named:)`](userdefaults/addsuite(named:).md) method to add the identifier for an unrelated app, the method doesn’t give you access to the other app’s settings. Instead, the system writes changes to your app’s settings, not to the third-party app’s settings.

> ❗ **Important**: An app that accesses settings in a suite must also have the [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups).

## Topics

### Creating a user defaults object
- [class var standard: UserDefaults](userdefaults/standard.md)
  The shared defaults object for the current app.
- [convenience init()](userdefaults/init.md)
  Creates a new defaults object and initializes it with the app’s current settings.
- [init?(suiteName: String?)](userdefaults/init(suitename:).md)
  Creates a new defaults object and initializes it with the settings from the specified database.
### Registering default settings
- [func register(defaults: [String : Any])](userdefaults/register(defaults:).md)
  Specifies the set of default settings and values to use as a fallback in cases where the app domain doesn’t have them.
### Getting the value of a key
- [func bool(forKey: String) -> Bool](userdefaults/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](userdefaults/integer(forkey:).md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](userdefaults/float(forkey:).md)
  Returns the floating-point value associated with the specified key.
- [func double(forKey: String) -> Double](userdefaults/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func url(forKey: String) -> URL?](userdefaults/url(forkey:).md)
  Returns the URL associated with the specified key.
- [func string(forKey: String) -> String?](userdefaults/string(forkey:).md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](userdefaults/stringarray(forkey:).md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](userdefaults/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](userdefaults/object(forkey:).md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](userdefaults/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](userdefaults/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [func dictionaryRepresentation() -> [String : Any]](userdefaults/dictionaryrepresentation.md)
  Returns a dictionary with the union of all key-value pairs found from all domains.
### Setting the value for a key
- [func set(Bool, forKey: String)](userdefaults/set(_:forkey:)-3nn5m.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Int, forKey: String)](userdefaults/set(_:forkey:)-3v852.md)
  Sets the value of the specified key to an integer.
- [func set(Float, forKey: String)](userdefaults/set(_:forkey:)-1t5ec.md)
  Sets the value of the specified key to a floating-point number.
- [func set(Double, forKey: String)](userdefaults/set(_:forkey:)-2w22f.md)
  Sets the value of the specified key to a double.
- [func set(URL?, forKey: String)](userdefaults/set(_:forkey:)-2bqjt.md)
  Sets the value of the specified key to a URL.
- [func set(Any?, forKey: String)](userdefaults/set(_:forkey:)-8ab6d.md)
  Sets the value of the specified key to a property list object.
### Monitoring settings changes and issues
- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)
- [class let didChangeNotification: NSNotification.Name](userdefaults/didchangenotification.md)
  Posted when the current process changes the value of a setting.
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)
- [class let sizeLimitExceededNotification: NSNotification.Name](userdefaults/sizelimitexceedednotification.md)
  Posted when the amount of data in the defaults database exceeds the allowed maximum.
### Removing settings values
- [func removeObject(forKey: String)](userdefaults/removeobject(forkey:).md)
  Removes the value for the specified key from the defaults database.
### Adding and removing search domains
- [func addSuite(named: String)](userdefaults/addsuite(named:).md)
  Inserts settings for the specified domain into the search list of the current object.
- [func removeSuite(named: String)](userdefaults/removesuite(named:).md)
  Removes the specified domain from the search list of the current object.
### Getting the domain names
- [class let argumentDomain: String](userdefaults/argumentdomain.md)
  The identifier for the domain that contains command-line settings.
- [class let globalDomain: String](userdefaults/globaldomain.md)
  The identifier for the domain that contains system-specified settings for all apps.
- [class let registrationDomain: String](userdefaults/registrationdomain.md)
  The identifier for the domain that contains your app’s registered default values.
- [var volatileDomainNames: [String]](userdefaults/volatiledomainnames.md)
  An array of identifiers for the volatile domains associated with the current object.
### Managing domain-specific values
- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Retrieves the settings from the specified persistent domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func volatileDomain(forName: String) -> [String : Any]](userdefaults/volatiledomain(forname:).md)
  Retrieves the settings from the specified volatile domain.
- [func setVolatileDomain([String : Any], forName: String)](userdefaults/setvolatiledomain(_:forname:).md)
  Replaces the keys and values in the specified domain with the new keys and values you supply.
- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the keys and values from the specified persistent domain.
- [func removeVolatileDomain(forName: String)](userdefaults/removevolatiledomain(forname:).md)
  Removes the keys and values from the specified volatile domain.
### Checking for managed keys
- [func objectIsForced(forKey: String) -> Bool](userdefaults/objectisforced(forkey:).md)
  Returns a Boolean value that indicates whether an administrator provided the value for the specified key.
- [func objectIsForced(forKey: String, inDomain: String) -> Bool](userdefaults/objectisforced(forkey:indomain:).md)
  Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.
### Deprecated
- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](userdefaults/synchronize.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](userdefaults/persistentdomainnames.md)
  Returns an array of the current persistent domain names.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.
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

## See Also

- [Accessing settings from your code](accessing-settings-from-your-code.md)
  Retrieve or change settings and monitor external changes to those values while your app runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults)*