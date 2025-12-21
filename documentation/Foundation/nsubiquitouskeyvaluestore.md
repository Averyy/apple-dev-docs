# NSUbiquitousKeyValueStore

**Framework**: Foundation  
**Kind**: class

An iCloud-based container of key-value pairs you share among instances of your app running on a person’s devices.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class NSUbiquitousKeyValueStore
```

#### Overview

Use the shared `NSUbiquitousKeyValueStore` object to store settings, configuration information, and app-specific data in a person’s iCloud account and share it among instances of your app running on all of the person’s devices. The object stores a dictionary of key-value pairs that you provide, and propagates that data to devices with the same Apple account. Sharing data among different devices gives you a way to coordinate your app’s behavior on those devices. For example, a textbook app might save the current page number on someone’s iPhone so that the person can continue reading from the same place on their other devices.

> ❗ **Important**: Don’t store personal or sensitive information in the key-value store. The system stores the information on disk in an unencrypted format. Store personal or sensitive information in the person’s Keychain instead.

Each app has a single iCloud key-value store object, which you retrieve from the [`default`](nsubiquitouskeyvaluestore/default.md) class property. Use this same object throughout your app to read and write values. Don’t subclass `NSUbiquitousKeyValueStore`.

> **Note**: To use this object, you must distribute your app through the App Store or Mac App Store, and you must request the [`iCloud Key-Value Store Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.ubiquity-kvstore-identifier) in your Xcode project.

The keys in the iCloud key-value store identify the item and its purpose in your app, and the value is a data object you use to implement the corresponding behavior in your app. Values must be property list types such as [`Int64`](https://developer.apple.com/documentation/Swift/Int64), [`Float`](https://developer.apple.com/documentation/Swift/Float), [`Double`](https://developer.apple.com/documentation/Swift/Double), [`Bool`](https://developer.apple.com/documentation/Swift/Bool), [`String`](https://developer.apple.com/documentation/Swift/String), [`NSNumber`](NSNumber.md), [`Date`](date.md), [`Array`](https://developer.apple.com/documentation/Swift/Array), or [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary). To include other types of objects in the key-value store, archive them to a [`Data`](data.md) object first and store that object instead. Prefer simple types over custom objects whenever possible.

When you write a new value, the iCloud key-value store saves it in memory initially and writes it to disk asynchronously later. If the device doesn’t have an active Apple account, the changes remain only on the current device. When the person signs into their account, the system forwards any changes to the iCloud server and reconciles the values there with the local ones. As you make more changes, the system keeps the local and server-based copies of the data synchronized, updating each one at appropriate times.

When a value changes on one device, iCloud forwards that change to the person’s other devices. If your app is running on one of those other devices, the system posts [`didChangeExternallyNotification`](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) to report the change. Register for that notification to keep all instances of your app in sync.

When designing the keys and values you intend to save for your app, consider the following size limitations:

- Your app can have no more than 1024 keys in the iCloud key-value store.
- The total amount of available storage space for all values is 1 megabyte.
- The maximum size for a single value is 1 megabyte. Therefore, if you associate 1 megabyte of data with a single key, you can’t write other keys to the store.
- The maximum length for each key string is 128 characters using the UTF-16 encoding. Key strings don’t count against the 1 megabyte quota for values.

If you exceed any of the prescribed limits during a write operation, the operation fails and the system doesn’t add the keys or values to the store. If a key string exceeds the maximum length, the system raises an exception. If a write operation would exceed your app’s quota, the system posts [`didChangeExternallyNotification`](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) notification with the change reason set to [`NSUbiquitousKeyValueStoreQuotaViolationChange`](nsubiquitouskeyvaluestorequotaviolationchange.md).

## Topics

### Getting the shared instance
- [class var `default`: NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore/default.md)
  The shared iCloud key-value store object.
### Getting values
- [func bool(forKey: String) -> Bool](nsubiquitouskeyvaluestore/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func double(forKey: String) -> Double](nsubiquitouskeyvaluestore/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](nsubiquitouskeyvaluestore/longlong(forkey:).md)
  Returns the 64-bit integer value associated with the specified key.
- [func string(forKey: String) -> String?](nsubiquitouskeyvaluestore/string(forkey:).md)
  Returns the string associated with the specified key.
- [func data(forKey: String) -> Data?](nsubiquitouskeyvaluestore/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](nsubiquitouskeyvaluestore/object(forkey:).md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](nsubiquitouskeyvaluestore/array(forkey:).md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](nsubiquitouskeyvaluestore/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [var dictionaryRepresentation: [String : Any]](nsubiquitouskeyvaluestore/dictionaryrepresentation.md)
  A dictionary with all of the key-value pairs in the iCloud key-value store.
### Setting values
- [func set(Bool, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Double, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-1xml0.md)
  Sets the value of the specified key to a double value.
- [func set(Int64, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-7tt20.md)
  Sets the value of the specified key to a 64-bit integer value.
- [func set(String?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-2rlp.md)
  Sets the value of the specified key to a string value.
- [func set(Data?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z.md)
  Sets the value of the specified key to a data object.
- [func set(Any?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9e3de.md)
  Sets the value of the specified key to a property list object.
- [func set([Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-40a8f.md)
  Sets the value of the specified key to an array of property list objects.
- [func set([String : Any]?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9vmlm.md)
  Sets the value of the specified key to a dictionary of property list objects.
### Synchronizing the in-memory cache with iCloud
- [func synchronize() -> Bool](nsubiquitouskeyvaluestore/synchronize.md)
  Synchronizes the in-memory keys and values with the ones stored in iCloud.
### Removing keys
- [func removeObject(forKey: String)](nsubiquitouskeyvaluestore/removeobject(forkey:).md)
  Removes the value for the specified key from the iCloud key-value store.
### Detecting changes to values
- [class let didChangeExternallyNotification: NSNotification.Name](nsubiquitouskeyvaluestore/didchangeexternallynotification.md)
  Posted when the value of one or more keys changes due to incoming data from iCloud.
- [let NSUbiquitousKeyValueStoreChangeReasonKey: String](nsubiquitouskeyvaluestorechangereasonkey.md)
  A key that indicates the reason why the key-value store changed.
- [let NSUbiquitousKeyValueStoreChangedKeysKey: String](nsubiquitouskeyvaluestorechangedkeyskey.md)
  A key that indicates which keys changed in the iCloud key-value store.
- [var NSUbiquitousKeyValueStoreServerChange: Int](nsubiquitouskeyvaluestoreserverchange.md)
  A constant that indicates a value changed in iCloud.
- [var NSUbiquitousKeyValueStoreInitialSyncChange: Int](nsubiquitouskeyvaluestoreinitialsyncchange.md)
  A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [var NSUbiquitousKeyValueStoreQuotaViolationChange: Int](nsubiquitouskeyvaluestorequotaviolationchange.md)
  A constant that indicates an attempt to write data exceeded the quota limits.
- [var NSUbiquitousKeyValueStoreAccountChange: Int](nsubiquitouskeyvaluestoreaccountchange.md)
  A constant that indicates the current Apple account changed.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)*