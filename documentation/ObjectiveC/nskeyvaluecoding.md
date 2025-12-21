# NSKeyValueCoding

**Framework**: Objective-C Runtime

A mechanism by which you can access the properties of an object indirectly by name or key.

#### Overview

The basic methods for accessing an object’s values are [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md), which sets the value for the property identified by the specified key, and [`value(forKey:)`](nsobject-swift.class/value(forkey:).md), which returns the value for the property identified by the specified key. Thus, all of an object’s properties can be accessed in a consistent manner.

The default implementation relies on the accessor methods normally implemented by objects (or to access instance variables directly if need be).

## Topics

### Getting Values
- [func value(forKey: String) -> Any?](nsobject-swift.class/value(forkey:).md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](nsobject-swift.class/value(forkeypath:).md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](nsobject-swift.class/dictionarywithvalues(forkeys:).md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func value(forUndefinedKey: String) -> Any?](nsobject-swift.class/value(forundefinedkey:).md)
  Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to a given key.
- [func mutableArrayValue(forKey: String) -> NSMutableArray](nsobject-swift.class/mutablearrayvalue(forkey:).md)
  Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [func mutableArrayValue(forKeyPath: String) -> NSMutableArray](nsobject-swift.class/mutablearrayvalue(forkeypath:).md)
  Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [func mutableSetValue(forKey: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkey:).md)
  Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [func mutableSetValue(forKeyPath: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkeypath:).md)
  Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [func mutableOrderedSetValue(forKey: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkey:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [func mutableOrderedSetValue(forKeyPath: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkeypath:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.
### Setting Values
- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](nsobject-swift.class/setvaluesforkeys(_:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setNilValueForKey(String)](nsobject-swift.class/setnilvalueforkey(_:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](nsobject-swift.class/setvalue(_:forkey:).md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](nsobject-swift.class/setvalue(_:forundefinedkey:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.
### Changing Default Behavior
- [class var accessInstanceVariablesDirectly: Bool](nsobject-swift.class/accessinstancevariablesdirectly.md)
  Returns a Boolean value that indicates whether the key-value coding methods should access the corresponding instance variable directly on finding no accessor method for a property.
### Validation
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](nsobject-swift.class/validatevalue(_:forkey:).md)
  Indicates whether the value specified by a given pointer is valid, or can be made valid, for the property identified by a given key.
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath: String) throws](nsobject-swift.class/validatevalue(_:forkeypath:).md)
  Indicates whether the value specified by a given pointer is not valid for a given key path relative to the receiver.
### Deprecated Methods
- [class func useStoredAccessor() -> Bool](nsobject-swift.class/usestoredaccessor.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](nsobject-swift.class/storedvalue(forkey:).md) and [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) should use private accessor methods in preference to public accessors.
- [func handleQuery(withUnboundKey: String) -> Any?](nsobject-swift.class/handlequery(withunboundkey:).md)
  Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to `key`.
- [func handleTakeValue(Any?, forUnboundKey: String)](nsobject-swift.class/handletakevalue(_:forunboundkey:).md)
  Invoked by [`takeValue(_:forKey:)`](nsobject-swift.class/takevalue(_:forkey:).md) when it finds no property binding for `key`.
- [func storedValue(forKey: String) -> Any?](nsobject-swift.class/storedvalue(forkey:).md)
  Returns the property identified by a given key.
- [func takeStoredValue(Any?, forKey: String)](nsobject-swift.class/takestoredvalue(_:forkey:).md)
  Sets the value of the property identified by a given key.
- [func takeValues(from: [AnyHashable : Any])](nsobject-swift.class/takevalues(from:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties
- [func takeValue(Any?, forKeyPath: String)](nsobject-swift.class/takevalue(_:forkeypath:).md)
  Sets the value for the property identified by `keyPath` to `value`.
- [func takeValue(Any?, forKey: String)](nsobject-swift.class/takevalue(_:forkey:).md)
  Sets the value for the property identified by `key` to `value`.
- [func unableToSetNil(forKey: String)](nsobject-swift.class/unabletosetnil(forkey:).md)
  Invoked if `key` is represented by a scalar attribute.
- [func values(forKeys: [Any]) -> [AnyHashable : Any]](nsobject-swift.class/values(forkeys:).md)
  Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.
### Constants
- [Key Value Coding Exception Names](key-value-coding-exception-names.md)
  This constant defines the name of an exception raised when a key value coding operation fails.
- [NSUndefinedKeyException userInfo Keys](nsundefinedkeyexception-userinfo-keys.md)
  These constants are keys into an `NSUndefinedKeyException` `userInfo` dictionary
- [var NSKeyValueValidationError: Int](../Foundation/NSKeyValueValidationError-swift.var.md)
  A key-value coding validation error.

## See Also

- [Key-Value Coding Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md)
  A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nskeyvaluecoding)*