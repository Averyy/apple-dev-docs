# JSValue

**Framework**: JavaScriptCore  
**Kind**: class  
**Role**: Class

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

```objc
@interface JSValue : NSObject
```

## Overview

You use the [`JSValue`](./jsvalue.md) class to convert basic values, such as numbers and strings, between JavaScript and Objective-C or Swift representations to pass data between native code and JavaScript code. You can also use this class to create JavaScript objects that wrap native objects of custom classes or JavaScript functions with implementations that native methods or blocks provide.

Each [`JSValue`](./jsvalue.md) instance originates from a [`JSContext`](./jscontext.md) object that represents the JavaScript execution environment containing that value. The value holds a strong reference to its [`context`](./jsvalue/context.md) object — as long as it retains any value for a particular [`JSContext`](./jscontext.md) instance, that context remains alive. When you invoke an instance method on a [`JSValue`](./jsvalue.md) object, and that method returns another [`JSValue`](./jsvalue.md) object, the returned value belongs to the same context as the original value.

Each JavaScript value also has an association (indirectly via the [`context`](./jsvalue/context.md) property) with a specific [`JSVirtualMachine`](./jsvirtualmachine.md) object that represents the underlying set of execution resources for its context. You can pass [`JSValue`](./jsvalue.md) instances only to methods on [`JSValue`](./jsvalue.md) and [`JSContext`](./jscontext.md) instances on the same virtual machine — attempting to pass a value to a different virtual machine raises an Objective-C exception.

### Convert Between JavaScript and Native Types

When you use the [`JSValue`](./jsvalue.md) methods for creating, reading, and converting JavaScript values, JavaScriptCore automatically converts native values to JavaScript values and vice versa, using the rules below.

- [`NSDictionary`](../Foundation/nsdictionary.md) objects or Swift dictionaries and the keys they contain become JavaScript objects with matching named properties and vice versa. JavaScriptCore recursively copies and converts the values for keys.
- [`NSArray`](../Foundation/nsarray.md) objects or Swift arrays become JavaScript arrays and vice versa, with elements that JavaScriptCore recursively copies and converts.
- Objective-C blocks (or Swift closures with the `@convention(block)` attribute) become JavaScript `Function` objects, with parameter and return types that JavaScriptCore converts using the same rules as values. Converting a JavaScript function with a backing from a native block or method returns that block or method; all other JavaScript functions convert as empty dictionaries.
- For all other native object types (and class types or metatypes), JavaScriptCore creates a JavaScript wrapper object with a constructor prototype chain that reflects the native class hierarchy. By default, the JavaScript wrapper for a native object doesn’t make that object’s properties and methods available in JavaScript. To choose properties and methods for export to JavaScript, see [`JSExport`](./jsexport.md).

When you convert an object, method, or block, JavaScriptCore implicitly converts the types and values of object properties and method parameters using the rules below:

| Objective-C (and Swift) types | JavaScript types | Notes |
| --- | --- | --- |
| `nil` | `undefined` |  |
| [`NSNull`](../Foundation/nsnull.md) | `null` |  |
| [`NSString`](../Foundation/nsstring.md) (Swift [`String`](../Swift/string.md)) | `String` |  |
| [`NSNumber`](../Foundation/nsnumber.md) and primitive numeric types | `Number`, `Boolean` | Conversion is consistent with the following methods: ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) [`init(int32:in:)`](./jsvalue/init%28int32,in%29.md) / [`toInt32()`](./jsvalue/toint32%28%29.md) for signed integer types ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) [`init(uInt32:in:)`](./jsvalue/init%28uint32,in%29.md) / [`toUInt32()`](./jsvalue/touint32%28%29.md) for unsigned integer types ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) [`init(bool:in:)`](./jsvalue/init%28bool,in%29.md) / [`toBool()`](./jsvalue/tobool%28%29.md) for Boolean types ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) [`init(double:in:)`](./jsvalue/init%28double,in%29.md) / [`toBool()`](./jsvalue/tobool%28%29.md) for all other numeric types |
| [`NSDictionary`](../Foundation/nsdictionary.md) (Swift [`Dictionary`](../Swift/dictionary.md)) | `Object` | Recursive conversion. |
| [`NSArray`](../Foundation/nsarray.md) (Swift [`Array`](../Swift/array.md)) | `Array` | Recursive conversion. |
| [`NSDate`](../Foundation/nsdate.md) | `Date` |  |
| Objective-C or Swift object ([`objc_object`](../ObjectiveC/objc_object.md) or [`AnyObject`](../Swift/anyobject.md)) ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) Objective-C or Swift class ([`Class`](../ObjectiveC/class.md) or [`AnyClass`](../Swift/anyclass.md)) | `Object` | Converts with [`init(object:in:)`](./jsvalue/init%28object,in%29.md) / [`toObject()`](./jsvalue/toobject%28%29.md). |
| Structure types: ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) [`NSRange`](../Foundation/nsrange-c.struct.md), [`CGRect`](../CoreFoundation/cgrect.md), [`CGPoint`](../CoreFoundation/cgpoint.md), [`CGSize`](../CoreFoundation/cgsize.md) | `Object` | There isn’t support for other structure types. |
| Objective-C block (Swift closure) | `Function` | Convert explicitly with [`init(object:in:)`](./jsvalue/init%28object,in%29.md) / [`toObject()`](./jsvalue/toobject%28%29.md). ![](https://developer.apple.com/tutorials/images/com.apple.javascriptcore/spacer.png) JavaScript functions don’t convert to native blocks/closures unless they already have a backing from a native block/closure. |

## Topics

### Creating JavaScript Values
- [init!(object: Any!, in: JSContext!)](./jsvalue/init%28object,in%29.md)
  Creates a JavaScript value by converting the specified native object.
- [init!(bool: Bool, in: JSContext!)](./jsvalue/init%28bool,in%29.md)
  Creates a JavaScript representation of the specified Boolean value.
- [init!(double: Double, in: JSContext!)](./jsvalue/init%28double,in%29.md)
  Creates a JavaScript representation of the specified floating-point value.
- [init!(int32: Int32, in: JSContext!)](./jsvalue/init%28int32,in%29.md)
  Creates a JavaScript representation of the specified signed integer value.
- [init!(uInt32: UInt32, in: JSContext!)](./jsvalue/init%28uint32,in%29.md)
  Creates a JavaScript representation of the specified unsigned integer value.
- [init!(newObjectIn: JSContext!)](./jsvalue/init%28newobjectin%29.md)
  Creates a new, empty JavaScript object value.
- [init!(newArrayIn: JSContext!)](./jsvalue/init%28newarrayin%29.md)
  Creates a new, empty JavaScript array value.
- [init!(newRegularExpressionFromPattern: String!, flags: String!, in: JSContext!)](./jsvalue/init%28newregularexpressionfrompattern,flags,in%29.md)
  Creates a JavaScript regular expression value from the specified pattern.
- [init!(newErrorFromMessage: String!, in: JSContext!)](./jsvalue/init%28newerrorfrommessage,in%29.md)
  Creates a JavaScript error value with the specified error message.
- [init!(undefinedIn: JSContext!)](./jsvalue/init%28undefinedin%29.md)
  Creates a JavaScript `undefined` value.
- [init!(nullIn: JSContext!)](./jsvalue/init%28nullin%29.md)
  Creates a JavaScript `null` value.
- [init!(point: CGPoint, inContext: JSContext!)](./jsvalue/init%28point,incontext%29.md)
  Creates a JavaScript representation of the specified point.
- [init!(range: NSRange, inContext: JSContext!)](./jsvalue/init%28range,incontext%29.md)
  Creates a JavaScript representation of the specified range.
- [init!(rect: CGRect, inContext: JSContext!)](./jsvalue/init%28rect,incontext%29.md)
  Creates a JavaScript representation of the specified rectangle.
- [init!(size: CGSize, inContext: JSContext!)](./jsvalue/init%28size,incontext%29.md)
  Creates a JavaScript representation of the specified width and height.
- [init!(newSymbolFromDescription: String!, in: JSContext!)](./jsvalue/init%28newsymbolfromdescription,in%29.md)
  Creates a unique symbol object.
- [init!(newPromiseIn: JSContext!, fromExecutor: ((JSValue?, JSValue?) -> Void)!)](./jsvalue/init%28newpromisein,fromexecutor%29.md)
  Creates a promise object using the specified executor callback.
- [init!(newPromiseRejectedWithReason: Any!, in: JSContext!)](./jsvalue/init%28newpromiserejectedwithreason,in%29.md)
  Creates a rejected promise object with the specified value.
- [init!(newPromiseResolvedWithResult: Any!, in: JSContext!)](./jsvalue/init%28newpromiseresolvedwithresult,in%29.md)
  Creates a resolved promise object with the specified value.
### Reading and Converting JavaScript Values
- [func toObject() -> Any!](./jsvalue/toobject%28%29.md)
  Converts the JavaScript value to a native object.
- [func toObjectOf(AnyClass!) -> Any!](./jsvalue/toobjectof%28_%29.md)
  Converts the JavaScript value to a native object of the specified class.
- [func toBool() -> Bool](./jsvalue/tobool%28%29.md)
  Converts the JavaScript value to a native Boolean value.
- [func toDouble() -> Double](./jsvalue/todouble%28%29.md)
  Converts the JavaScript value to a native floating-point value.
- [func toInt32() -> Int32](./jsvalue/toint32%28%29.md)
  Converts the JavaScript value to a native signed integer value.
- [func toUInt32() -> UInt32](./jsvalue/touint32%28%29.md)
  Converts the JavaScript value to a native unsigned integer value.
- [func toNumber() -> NSNumber!](./jsvalue/tonumber%28%29.md)
  Converts the JavaScript value to a [`NSNumber`](../Foundation/nsnumber.md) object.
- [func toString() -> String!](./jsvalue/tostring%28%29.md)
  Converts the JavaScript value to a native string.
- [func toDate() -> Date!](./jsvalue/todate%28%29.md)
  Converts the JavaScript value to a date object.
- [func toArray() -> [Any]!](./jsvalue/toarray%28%29.md)
  Converts the JavaScript value to an array.
- [func toDictionary() -> [AnyHashable : Any]!](./jsvalue/todictionary%28%29.md)
  Converts the JavaScript value to a dictionary.
- [func toPoint() -> CGPoint](./jsvalue/topoint%28%29.md)
  Converts the value to a point structure.
- [func toRange() -> NSRange](./jsvalue/torange%28%29.md)
  Converts the value to a range.
- [func toRect() -> CGRect](./jsvalue/torect%28%29.md)
  Converts the value to a rectangle structure.
- [func toSize() -> CGSize](./jsvalue/tosize%28%29.md)
  Converts the value to a size.
### Determining the Type of a JavaScript Value
- [var isUndefined: Bool](./jsvalue/isundefined.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `undefined` value.
- [var isNull: Bool](./jsvalue/isnull.md)
  A Boolean value that indicates whether the instance corresponds to the JavaScript `null` value.
- [var isBoolean: Bool](./jsvalue/isboolean.md)
  A Boolean value that indicates whether the instance is a JavaScript Boolean value.
- [var isNumber: Bool](./jsvalue/isnumber.md)
  A Boolean value that indicates whether the instance is a JavaScript numeric value.
- [var isString: Bool](./jsvalue/isstring.md)
  A Boolean value that indicates whether the instance is a JavaScript `String` object.
- [var isObject: Bool](./jsvalue/isobject.md)
  A Boolean value that indicates whether the instance is a JavaScript object.
- [var isArray: Bool](./jsvalue/isarray.md)
  A Boolean value that indicates whether the instance is a JavaScript array value.
- [var isDate: Bool](./jsvalue/isdate.md)
  A Boolean value that indicates whether the instance is a JavaScript `Date` object.
- [var isSymbol: Bool](./jsvalue/issymbol.md)
  A Boolean value that indicates whether the instance is a symbol.
### Comparing JavaScript Values
- [func isEqual(to: Any!) -> Bool](./jsvalue/isequal%28to%29.md)
  Compares the value to another for strict equality.
- [func isEqualWithTypeCoercion(to: Any!) -> Bool](./jsvalue/isequalwithtypecoercion%28to%29.md)
  Compares the value to another for equivalence, allowing type conversion.
- [func isInstance(of: Any!) -> Bool](./jsvalue/isinstance%28of%29.md)
  Returns a Boolean value indicating whether the value is an instance of another JavaScript object value.
### Working with Function and Constructor Values
- [func call(withArguments: [Any]!) -> JSValue!](./jsvalue/call%28witharguments%29.md)
  Invokes the value as a JavaScript function.
- [func construct(withArguments: [Any]!) -> JSValue!](./jsvalue/construct%28witharguments%29.md)
  Invokes the value as a JavaScript constructor.
- [func invokeMethod(String!, withArguments: [Any]!) -> JSValue!](./jsvalue/invokemethod%28_,witharguments%29.md)
  Calls the named JavaScript method on the value.
### Working with Container Values
- [func defineProperty(Any!, descriptor: Any!)](./jsvalue/defineproperty%28_,descriptor%29.md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](./jsvalue/hasproperty%28_%29.md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](./jsvalue/deleteproperty%28_%29.md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](./jsvalue/atindex%28_%29.md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](./jsvalue/setvalue%28_,at%29.md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](./jsvalue/forproperty%28_%29.md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](./jsvalue/setvalue%28_,forproperty%29.md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](./jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.
### Accessing a Value’s JavaScript Context
- [var context: JSContext!](./jsvalue/context.md)
  The JavaScript context hosting this value.
### Accessing Values with Subscript Syntax
- [func objectAtIndexedSubscript(Int) -> JSValue!](./jsvalue/objectatindexedsubscript%28_%29.md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func setObject(Any!, atIndexedSubscript: Int)](./jsvalue/setobject%28_,atindexedsubscript%29.md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func objectForKeyedSubscript(Any!) -> JSValue!](./jsvalue/objectforkeyedsubscript%28_%29.md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.
- [func setObject(Any!, forKeyedSubscript: Any!)](./jsvalue/setobject%28_,forkeyedsubscript%29.md)
  Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.
### Working with the C JavaScriptCore API
- [var jsValueRef: JSValueRef!](./jsvalue/jsvalueref.md)
  Returns the C representation of the JavaScript value.
- [init!(JSValueRef: JSValueRef!, inContext: JSContext!)](./jsvalue/init%28jsvalueref,incontext%29.md)
  Creates a JavaScript value object from the equivalent C representation.
### Constants
- [Property Descriptor Keys](./property-descriptor-keys.md)
  Keys for the native dictionary representation of a JavaScript property descriptor, used with the [`defineProperty(_:descriptor:)`](./jsvalue/defineproperty%28_,descriptor%29.md) method.
### Initializers
- [init!(UInt32: UInt32, inContext: JSContext!)](./jsvalue/init%28uint32,incontext%29.md)
- [init!(bool: Bool, inContext: JSContext!)](./jsvalue/init%28bool,incontext%29.md)
- [init!(double: Double, inContext: JSContext!)](./jsvalue/init%28double,incontext%29.md)
- [init!(int32: Int32, inContext: JSContext!)](./jsvalue/init%28int32,incontext%29.md)
- [init!(jsValueRef: JSValueRef!, in: JSContext!)](./jsvalue/init%28jsvalueref,in%29.md)
- [init!(newArrayInContext: JSContext!)](./jsvalue/init%28newarrayincontext%29.md)
- [init?(newBigIntFrom: String, in: JSContext)](./jsvalue/init%28newbigintfrom,in%29-1f0xs.md)
- [init?(newBigIntFrom: UInt64, in: JSContext)](./jsvalue/init%28newbigintfrom,in%29-7worq.md)
- [init?(newBigIntFrom: Int64, in: JSContext)](./jsvalue/init%28newbigintfrom,in%29-8l9iv.md)
- [init?(newBigIntFrom: Double, in: JSContext)](./jsvalue/init%28newbigintfrom,in%29-r38z.md)
- [init?(newBigIntFromDouble: Double, inContext: JSContext)](./jsvalue/init%28newbigintfromdouble,incontext%29.md)
- [init?(newBigIntFromInt64: Int64, inContext: JSContext)](./jsvalue/init%28newbigintfromint64,incontext%29.md)
- [init?(newBigIntFromString: String, inContext: JSContext)](./jsvalue/init%28newbigintfromstring,incontext%29.md)
- [init?(newBigIntFromUInt64: UInt64, inContext: JSContext)](./jsvalue/init%28newbigintfromuint64,incontext%29.md)
- [init!(newErrorFromMessage: String!, inContext: JSContext!)](./jsvalue/init%28newerrorfrommessage,incontext%29.md)
- [init!(newObjectInContext: JSContext!)](./jsvalue/init%28newobjectincontext%29.md)
- [init!(newPromiseInContext: JSContext!, fromExecutor: ((JSValue?, JSValue?) -> Void)!)](./jsvalue/init%28newpromiseincontext,fromexecutor%29.md)
- [init!(newPromiseRejectedWithReason: Any!, inContext: JSContext!)](./jsvalue/init%28newpromiserejectedwithreason,incontext%29.md)
- [init!(newPromiseResolvedWithResult: Any!, inContext: JSContext!)](./jsvalue/init%28newpromiseresolvedwithresult,incontext%29.md)
- [init!(newRegularExpressionFromPattern: String!, flags: String!, inContext: JSContext!)](./jsvalue/init%28newregularexpressionfrompattern,flags,incontext%29.md)
- [init!(newSymbolFromDescription: String!, inContext: JSContext!)](./jsvalue/init%28newsymbolfromdescription,incontext%29.md)
- [init!(nullInContext: JSContext!)](./jsvalue/init%28nullincontext%29.md)
- [init!(object: Any!, inContext: JSContext!)](./jsvalue/init%28object,incontext%29.md)
- [init!(point: CGPoint, in: JSContext!)](./jsvalue/init%28point,in%29.md)
- [init!(range: NSRange, in: JSContext!)](./jsvalue/init%28range,in%29.md)
- [init!(rect: CGRect, in: JSContext!)](./jsvalue/init%28rect,in%29.md)
- [init!(size: CGSize, in: JSContext!)](./jsvalue/init%28size,in%29.md)
- [init!(undefinedInContext: JSContext!)](./jsvalue/init%28undefinedincontext%29.md)
### Instance Properties
- [var isBigInt: Bool](./jsvalue/isbigint.md)
### Instance Methods
- [func compare(Double) -> JSRelationCondition](./jsvalue/compare%28_%29-35b2t.md)
- [func compare(JSValue) -> JSRelationCondition](./jsvalue/compare%28_%29-5w184.md)
- [func compare(UInt64) -> JSRelationCondition](./jsvalue/compare%28_%29-64n3k.md)
- [func compare(Int64) -> JSRelationCondition](./jsvalue/compare%28_%29-9d4zq.md)
- [func toInt64() -> Int64](./jsvalue/toint64%28%29.md)
- [func toUInt64() -> UInt64](./jsvalue/touint64%28%29.md)
### Default Implementations
- [JSValue Implementations](./jsvalue/jsvalue-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### JavaScript Code
- [class JSManagedValue](./jsmanagedvalue.md)
  A JavaScript value with conditional retain behavior to provide automatic memory management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue)*