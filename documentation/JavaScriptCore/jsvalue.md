# JSValue

**Framework**: JavaScriptCore  
**Kind**: class

A JavaScript value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class JSValue
```

#### Overview

You use the [`JSValue`](jsvalue.md) class to convert basic values, such as numbers and strings, between JavaScript and Objective-C or Swift representations to pass data between native code and JavaScript code. You can also use this class to create JavaScript objects that wrap native objects of custom classes or JavaScript functions with implementations that native methods or blocks provide.

Each [`JSValue`](jsvalue.md) instance originates from a [`JSContext`](jscontext.md) object that represents the JavaScript execution environment containing that value. The value holds a strong reference to its [`context`](jsvalue/context.md) object — as long as it retains any value for a particular [`JSContext`](jscontext.md) instance, that context remains alive. When you invoke an instance method on a [`JSValue`](jsvalue.md) object, and that method returns another [`JSValue`](jsvalue.md) object, the returned value belongs to the same context as the original value.

Each JavaScript value also has an association (indirectly via the [`context`](jsvalue/context.md) property) with a specific [`JSVirtualMachine`](jsvirtualmachine.md) object that represents the underlying set of execution resources for its context. You can pass [`JSValue`](jsvalue.md) instances only to methods on [`JSValue`](jsvalue.md) and [`JSContext`](jscontext.md) instances on the same virtual machine — attempting to pass a value to a different virtual machine raises an Objective-C exception.

##### Convert Between Javascript and Native Types

When you use the [`JSValue`](jsvalue.md) methods for creating, reading, and converting JavaScript values, JavaScriptCore automatically converts native values to JavaScript values and vice versa, using the rules below.

- [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) objects or Swift dictionaries and the keys they contain become JavaScript objects with matching named properties and vice versa. JavaScriptCore recursively copies and converts the values for keys.
- [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) objects or Swift arrays become JavaScript arrays and vice versa, with elements that JavaScriptCore recursively copies and converts.
- Objective-C blocks (or Swift closures with the `@convention(block)` attribute) become JavaScript `Function` objects, with parameter and return types that JavaScriptCore converts using the same rules as values. Converting a JavaScript function with a backing from a native block or method returns that block or method; all other JavaScript functions convert as empty dictionaries.
- For all other native object types (and class types or metatypes), JavaScriptCore creates a JavaScript wrapper object with a constructor prototype chain that reflects the native class hierarchy. By default, the JavaScript wrapper for a native object doesn’t make that object’s properties and methods available in JavaScript. To choose properties and methods for export to JavaScript, see [`JSExport`](jsexport.md).

When you convert an object, method, or block, JavaScriptCore implicitly converts the types and values of object properties and method parameters using the rules below:

| Objective-C (and Swift) types | JavaScript types | Notes |
| --- | --- | --- |
| `nil` | `undefined` |  |
| [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) | `null` |  |
| [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) (Swift [`String`](https://developer.apple.com/documentation/Swift/String)) | `String` |  |
| [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) and primitive numeric types | `Number`, `Boolean` | Conversion is consistent with the following methods: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`init(int32:in:)`](jsvalue/init(int32:in:).md) / [`toInt32()`](jsvalue/toint32().md) for signed integer types ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`init(uInt32:in:)`](jsvalue/init(uint32:in:).md) / [`toUInt32()`](jsvalue/touint32().md) for unsigned integer types ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`init(bool:in:)`](jsvalue/init(bool:in:).md) / [`toBool()`](jsvalue/tobool().md) for Boolean types ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`init(double:in:)`](jsvalue/init(double:in:).md) / [`toBool()`](jsvalue/tobool().md) for all other numeric types |
| [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) (Swift [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary)) | `Object` | Recursive conversion. |
| [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) (Swift [`Array`](https://developer.apple.com/documentation/Swift/Array)) | `Array` | Recursive conversion. |
| [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) | `Date` |  |
| Objective-C or Swift object ([`objc_object`](https://developer.apple.com/documentation/ObjectiveC/objc_object) or [`AnyObject`](https://developer.apple.com/documentation/Swift/AnyObject)) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Objective-C or Swift class ([`Class`](https://developer.apple.com/documentation/ObjectiveC/Class) or [`AnyClass`](https://developer.apple.com/documentation/Swift/AnyClass)) | `Object` | Converts with [`init(object:in:)`](jsvalue/init(object:in:).md) / [`toObject()`](jsvalue/toobject().md). |
| Structure types: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange), [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect), [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint), [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) | `Object` | There isn’t support for other structure types. |
| Objective-C block (Swift closure) | `Function` | Convert explicitly with [`init(object:in:)`](jsvalue/init(object:in:).md) / [`toObject()`](jsvalue/toobject().md). ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) JavaScript functions don’t convert to native blocks/closures unless they already have a backing from a native block/closure. |

## Topics

### Creating JavaScript Values
- [init!(object: Any!, in: JSContext!)](jsvalue/init(object:in:).md)
  Creates a JavaScript value by converting the specified native object.
- [init!(bool: Bool, in: JSContext!)](jsvalue/init(bool:in:).md)
  Creates a JavaScript representation of the specified Boolean value.
- [init!(double: Double, in: JSContext!)](jsvalue/init(double:in:).md)
  Creates a JavaScript representation of the specified floating-point value.
- [init!(int32: Int32, in: JSContext!)](jsvalue/init(int32:in:).md)
  Creates a JavaScript representation of the specified signed integer value.
- [init!(uInt32: UInt32, in: JSContext!)](jsvalue/init(uint32:in:).md)
  Creates a JavaScript representation of the specified unsigned integer value.
- [init!(newObjectIn: JSContext!)](jsvalue/init(newobjectin:).md)
  Creates a new, empty JavaScript object value.
- [init!(newArrayIn: JSContext!)](jsvalue/init(newarrayin:).md)
  Creates a new, empty JavaScript array value.
- [init!(newRegularExpressionFromPattern: String!, flags: String!, in: JSContext!)](jsvalue/init(newregularexpressionfrompattern:flags:in:).md)
  Creates a JavaScript regular expression value from the specified pattern.
- [init!(newErrorFromMessage: String!, in: JSContext!)](jsvalue/init(newerrorfrommessage:in:).md)
  Creates a JavaScript error value with the specified error message.
- [init!(undefinedIn: JSContext!)](jsvalue/init(undefinedin:).md)
  Creates a JavaScript `undefined` value.
- [init!(nullIn: JSContext!)](jsvalue/init(nullin:).md)
  Creates a JavaScript `null` value.
- [init!(point: CGPoint, inContext: JSContext!)](jsvalue/init(point:incontext:).md)
  Creates a JavaScript representation of the specified point.
- [init!(range: NSRange, inContext: JSContext!)](jsvalue/init(range:incontext:).md)
  Creates a JavaScript representation of the specified range.
- [init!(rect: CGRect, inContext: JSContext!)](jsvalue/init(rect:incontext:).md)
  Creates a JavaScript representation of the specified rectangle.
- [init!(size: CGSize, inContext: JSContext!)](jsvalue/init(size:incontext:).md)
  Creates a JavaScript representation of the specified width and height.
- [init!(newSymbolFromDescription: String!, in: JSContext!)](jsvalue/init(newsymbolfromdescription:in:).md)
  Creates a unique symbol object.
- [init!(newPromiseIn: JSContext!, fromExecutor: ((JSValue?, JSValue?) -> Void)!)](jsvalue/init(newpromisein:fromexecutor:).md)
  Creates a promise object using the specified executor callback.
- [init!(newPromiseRejectedWithReason: Any!, in: JSContext!)](jsvalue/init(newpromiserejectedwithreason:in:).md)
  Creates a rejected promise object with the specified value.
- [init!(newPromiseResolvedWithResult: Any!, in: JSContext!)](jsvalue/init(newpromiseresolvedwithresult:in:).md)
  Creates a resolved promise object with the specified value.
### Reading and Converting JavaScript Values
- [func toObject() -> Any!](jsvalue/toobject.md)
  Converts the JavaScript value to a native object.
- [func toObjectOf(AnyClass!) -> Any!](jsvalue/toobjectof(_:).md)
  Converts the JavaScript value to a native object of the specified class.
- [func toBool() -> Bool](jsvalue/tobool.md)
  Converts the JavaScript value to a native Boolean value.
- [func toDouble() -> Double](jsvalue/todouble.md)
  Converts the JavaScript value to a native floating-point value.
- [func toInt32() -> Int32](jsvalue/toint32.md)
  Converts the JavaScript value to a native signed integer value.
- [func toUInt32() -> UInt32](jsvalue/touint32.md)
  Converts the JavaScript value to a native unsigned integer value.
- [func toNumber() -> NSNumber!](jsvalue/tonumber.md)
  Converts the JavaScript value to a [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object.
- [func toString() -> String!](jsvalue/tostring.md)
  Converts the JavaScript value to a native string.
- [func toDate() -> Date!](jsvalue/todate.md)
  Converts the JavaScript value to a date object.
- [func toArray() -> [Any]!](jsvalue/toarray.md)
  Converts the JavaScript value to an array.
- [func toDictionary() -> [AnyHashable : Any]!](jsvalue/todictionary.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](jsvalue/topoint.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](jsvalue/torange.md)
  Converts the value to a range.
- [func toRect() -> CGRect](jsvalue/torect.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](jsvalue/tosize.md)
  Converts the value to a size.
### Determining the Type of a JavaScript Value
- [var isUndefined: Bool](jsvalue/isundefined.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `undefined` value.
- [var isNull: Bool](jsvalue/isnull.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `null` value.
- [var isBoolean: Bool](jsvalue/isboolean.md)
  A Boolean value that indicates whether the instance is a JavaScript Boolean value.
- [var isNumber: Bool](jsvalue/isnumber.md)
  A Boolean value that indicates whether the instance is a JavaScript numeric value.
- [var isString: Bool](jsvalue/isstring.md)
  A Boolean value that indicates whether the instance is a JavaScript `String` object.
- [var isObject: Bool](jsvalue/isobject.md)
  A Boolean value that indicates whether the instance is a JavaScript object.
- [var isArray: Bool](jsvalue/isarray.md)
  A Boolean value that indicates whether the instance is a JavaScript array value.
- [var isDate: Bool](jsvalue/isdate.md)
  A Boolean value that indicates whether the instance is a JavaScript `Date` object.
- [var isSymbol: Bool](jsvalue/issymbol.md)
  A Boolean value that indicates whether the instance is a symbol.
### Comparing JavaScript Values
- [func isEqual(to: Any!) -> Bool](jsvalue/isequal(to:).md)
  Compares the value to another for strict equality.
- [func isEqualWithTypeCoercion(to: Any!) -> Bool](jsvalue/isequalwithtypecoercion(to:).md)
  Compares the value to another for equivalence, allowing type conversion.
- [func isInstance(of: Any!) -> Bool](jsvalue/isinstance(of:).md)
  Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.
### Working with Function and Constructor Values
- [func call(withArguments: [Any]!) -> JSValue!](jsvalue/call(witharguments:).md)
  Invokes the value as a JavaScript function.
- [func construct(withArguments: [Any]!) -> JSValue!](jsvalue/construct(witharguments:).md)
  Invokes the value as a JavaScript constructor.
- [func invokeMethod(String!, withArguments: [Any]!) -> JSValue!](jsvalue/invokemethod(_:witharguments:).md)
  Calls the named JavaScript method on the value.
### Working with Container Values
- [func defineProperty(Any!, descriptor: Any!)](jsvalue/defineproperty(_:descriptor:).md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](jsvalue/hasproperty(_:).md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](jsvalue/deleteproperty(_:).md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](jsvalue/atindex(_:).md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](jsvalue/setvalue(_:at:).md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](jsvalue/forproperty(_:).md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](jsvalue/setvalue(_:forproperty:).md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.
### Accessing a Value’s JavaScript Context
- [var context: JSContext!](jsvalue/context.md)
  The JavaScript context hosting this value.
### Accessing Values with Subscript Syntax
- [func objectAtIndexedSubscript(Int) -> JSValue!](jsvalue/objectatindexedsubscript(_:).md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func setObject(Any!, atIndexedSubscript: Int)](jsvalue/setobject(_:atindexedsubscript:).md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func objectForKeyedSubscript(Any!) -> JSValue!](jsvalue/objectforkeyedsubscript(_:).md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.
- [func setObject(Any!, forKeyedSubscript: Any!)](jsvalue/setobject(_:forkeyedsubscript:).md)
  Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.
### Working with the C JavaScriptCore API
- [var jsValueRef: JSValueRef!](jsvalue/jsvalueref.md)
  Returns the C representation of the JavaScript value.
- [init!(JSValueRef: JSValueRef!, inContext: JSContext!)](jsvalue/init(jsvalueref:incontext:).md)
  Creates a JavaScript value object from the equivalent C representation.
### Constants
- [Property Descriptor Keys](property-descriptor-keys.md)
  Keys for the native dictionary representation of a JavaScript property descriptor, used with the [`defineProperty(_:descriptor:)`](jsvalue/defineproperty(_:descriptor:).md) method.
### Initializers
- [init?(newBigIntFrom: String, in: JSContext)](jsvalue/init(newbigintfrom:in:)-1f0xs.md)
- [init?(newBigIntFrom: UInt64, in: JSContext)](jsvalue/init(newbigintfrom:in:)-7worq.md)
- [init?(newBigIntFrom: Int64, in: JSContext)](jsvalue/init(newbigintfrom:in:)-8l9iv.md)
- [init?(newBigIntFrom: Double, in: JSContext)](jsvalue/init(newbigintfrom:in:)-r38z.md)
### Instance Properties
- [var isBigInt: Bool](jsvalue/isbigint.md)
### Instance Methods
- [func compare(Double) -> JSRelationCondition](jsvalue/compare(_:)-35b2t.md)
- [func compare(JSValue) -> JSRelationCondition](jsvalue/compare(_:)-5w184.md)
- [func compare(UInt64) -> JSRelationCondition](jsvalue/compare(_:)-64n3k.md)
- [func compare(Int64) -> JSRelationCondition](jsvalue/compare(_:)-9d4zq.md)
- [func toInt64() -> Int64](jsvalue/toint64.md)
- [func toUInt64() -> UInt64](jsvalue/touint64.md)

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

- [class JSManagedValue](jsmanagedvalue.md)
  A JavaScript value with conditional retain behavior to provide automatic memory management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue)*