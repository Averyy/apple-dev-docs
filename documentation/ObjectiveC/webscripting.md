# WebScripting

**Framework**: Objective-C Runtime

`WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.

#### Overview

Not all properties and methods are exported to JavaScript by default. The object needs to implement the class methods described below to specify the properties and methods to export. Furthermore, a method is not exported if its return type and all its parameters are not Objective-C objects or scalars.

Method argument and return types that are Objective-C objects will be converted to appropriate types for the scripting environment. For example:

- `nil` is converted to undefined.
- `NSNumber` objects will be converted to JavaScript numbers.
- `NSString` objects will be converted to JavaScript strings.
- `NSArray` objects will be mapped to special read-only arrays.
- `NSNull` will be converted to JavaScript’s `null`.
- `WebUndefined` will be converted to undefined.
- `WebScriptObject` instances will be unwrapped for the scripting environment.

Instances of all other classes will be wrapped before being passed to the script, and unwrapped as they return to Objective-C. Primitive types such as `int` and `char` are cast to a numeric in JavaScript.

Access to an object’s attributes, such as instance variables, is managed by key-value coding (KVC). The KVC methods `setValue:forKey:` and `valueForKey:` are used to access the attributes of an object from the scripting environment. Additionally, the scripting environment can attempt any number of attribute requests or method invocations that are not exported by your class. You can manage these requests by overriding the `setValue:forUndefinedKey:` and `valueForUndefinedKey:` methods from the key-value coding protocol.

Exceptions can be raised from the scripting environment by sending a [`throwException(_:)`](https://developer.apple.com/documentation/WebKit/WebScriptObject/throwException(_:)) message to the relevant `WebScriptObject` instance. The method raising the exception must be within the scope of the script invocation.

## Topics

### Getting attributes
- [class func webScriptName(forKey: UnsafePointer<CChar>!) -> String!](nsobject-swift.class/webscriptname(forkey:).md)
  Returns the scripting environment name for an attribute specified by a key.
- [class func webScriptName(for: Selector!) -> String!](nsobject-swift.class/webscriptname(for:).md)
  Returns the scripting environment name for a selector.
- [class func isSelectorExcluded(fromWebScript: Selector!) -> Bool](nsobject-swift.class/isselectorexcluded(fromwebscript:).md)
  Returns whether a selector should be hidden from the scripting environment.
- [class func isKeyExcluded(fromWebScript: UnsafePointer<CChar>!) -> Bool](nsobject-swift.class/iskeyexcluded(fromwebscript:).md)
  Returns whether a key should be hidden from the scripting environment.
### Invoking methods
- [func invokeDefaultMethod(withArguments: [Any]!) -> Any!](nsobject-swift.class/invokedefaultmethod(witharguments:).md)
  Executes when a script attempts to invoke a method on an exposed object directly.
- [func invokeUndefinedMethod(fromWebScript: String!, withArguments: [Any]!) -> Any!](nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:).md)
  Handles undefined method invocation from the scripting environment.
### Finalizing
- [func finalizeForWebScript()](nsobject-swift.class/finalizeforwebscript.md)
  Performs cleanup when the scripting environment is reset.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/webscripting)*