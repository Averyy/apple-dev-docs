# NSKeyValueCoding

**Framework**: Objective-C Runtime

A mechanism by which you can access the properties of an object indirectly by name or key.

#### Overview

The basic methods for accessing an object’s values are `NSObject-class/setValue(_:forKey:)`, which sets the value for the property identified by the specified key, and `NSObject-class/value(forKey:)`, which returns the value for the property identified by the specified key. Thus, all of an object’s properties can be accessed in a consistent manner.

The default implementation relies on the accessor methods normally implemented by objects (or to access instance variables directly if need be).

## Topics

### Constants
- [Key Value Coding Exception Names](key-value-coding-exception-names.md)
  This constant defines the name of an exception raised when a key value coding operation fails.
- [NSUndefinedKeyException userInfo Keys](nsundefinedkeyexception-userinfo-keys.md)
  These constants are keys into an `NSUndefinedKeyException` `userInfo` dictionary
- [var NSKeyValueValidationError: Int { get }](../Foundation/NSKeyValueValidationError-swift.var.md)
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