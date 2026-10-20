# NSScriptKeyValueCoding

**Framework**: Objective-C Runtime  
**Role**: API Collection

A collection of methods that provide additional capabilities for working with key-value coding.

#### Overview

Cocoa scripting takes advantage of key-value coding to get and set information in scriptable objects. The methods in this category provide additional capabilities for working with key-value coding, including getting and setting key values by index in multi-value keys and coercing (or converting) a key value. Additional methods allow the implementer of a scriptable container class to provide fast access to elements that are being referenced by name and unique ID.

Because Cocoa scripting invokes [`setValue(_:forKey:)`](./nsobject-swift.class/setvalue%28_,forkey%29.md) and [`mutableArrayValue(forKey:)`](./nsobject-swift.class/mutablearrayvalue%28forkey%29.md), changes to model objects made by AppleScript scripts are observable using automatic key-value observing.

> **Note**:  In OS X 10.3 and earlier, Cocoa scripting did not invoke [`setValue(_:forKey:)`](./nsobject-swift.class/setvalue%28_,forkey%29.md) or [`mutableArrayValue(forKey:)`](./nsobject-swift.class/mutablearrayvalue%28forkey%29.md), so automatic key-value observing notification was not always done for model object changes caused by scripts. Starting in macOS 10.4, for backward binary compatibility, if it is overridden, Cocoa invokes the now-deprecated method [`takeValue(_:forKey:)`](./nsobject-swift.class/takevalue%28_,forkey%29.md) instead of [`setValue(_:forKey:)`](./nsobject-swift.class/setvalue%28_,forkey%29.md).

## Topics

### Indexed access
- [func insertValue(Any, at: Int, inPropertyWithKey: String)](./nsobject-swift.class/insertvalue%28_,at,inpropertywithkey%29.md)
  Inserts an object at the specified index in the collection specified by the passed key.
- [func removeValue(at: Int, fromPropertyWithKey: String)](./nsobject-swift.class/removevalue%28at,frompropertywithkey%29.md)
  Removes the object at the specified index from the collection specified by the passed key.
- [func replaceValue(at: Int, inPropertyWithKey: String, withValue: Any)](./nsobject-swift.class/replacevalue%28at,inpropertywithkey,withvalue%29.md)
  Replaces the object at the specified index in the collection specified by the passed key.
- [func value(at: Int, inPropertyWithKey: String) -> Any?](./nsobject-swift.class/value%28at,inpropertywithkey%29.md)
  Retrieves an indexed object from the collection specified by the passed key.
### Access by name, key, or ID
- [func insertValue(Any, inPropertyWithKey: String)](./nsobject-swift.class/insertvalue%28_,inpropertywithkey%29.md)
  Inserts an object in the collection specified by the passed key.
- [func value(withName: String, inPropertyWithKey: String) -> Any?](./nsobject-swift.class/value%28withname,inpropertywithkey%29.md)
  Retrieves a named object from the collection specified by the passed key.
- [func value(withUniqueID: Any, inPropertyWithKey: String) -> Any?](./nsobject-swift.class/value%28withuniqueid,inpropertywithkey%29.md)
  Retrieves an object by ID from the collection specified by the passed key.
### Coercion
- [func coerceValue(Any?, forKey: String) -> Any?](./nsobject-swift.class/coercevalue%28_,forkey%29.md)
  Uses type info from the class description and `NSScriptCoercionHandler` to attempt to convert `value` for `key` to the proper type, if necessary.
### Constants
- [NSScriptKeyValueCoding Exception Names](./nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
### Key-Value Coding
- [NSKeyValueBindingCreation](./nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSKeyValueCoding](./nskeyvaluecoding.md)
  A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding Exception Names](./nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsscriptkeyvaluecoding)*