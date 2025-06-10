# NSScriptKeyValueCoding

**Framework**: Objective-C Runtime

A collection of methods that provide additional capabilities for working with key-value coding.

#### Overview

Cocoa scripting takes advantage of key-value coding to get and set information in scriptable objects. The methods in this category provide additional capabilities for working with key-value coding, including getting and setting key values by index in multi-value keys and coercing (or converting) a key value. Additional methods allow the implementer of a scriptable container class to provide fast access to elements that are being referenced by name and unique ID.

Because Cocoa scripting invokes `NSObject-class/setValue(_:forKey:)` and `NSObject-class/mutableArrayValue(forKey:)`, changes to model objects made by AppleScript scripts are observable using automatic key-value observing.

> **Note**:  In OS X 10.3 and earlier, Cocoa scripting did not invoke `NSObject-class/setValue(_:forKey:)` or `NSObject-class/mutableArrayValue(forKey:)`, so automatic key-value observing notification was not always done for model object changes caused by scripts. Starting in macOS 10.4, for backward binary compatibility, if it is overridden, Cocoa invokes the now-deprecated method `NSObject-class/takeValue(_:forKey:)` instead of `NSObject-class/setValue(_:forKey:)`.

## Topics

### Constants
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md)
  A set of methods that you can use to create and remove bindings between view objects and controllers, or between controllers and model objects.
- [NSKeyValueCoding](nskeyvaluecoding.md)
  A mechanism by which you can access the properties of an object indirectly by name or key.
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md)
  Exceptions raised by key-value coding methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsscriptkeyvaluecoding)*