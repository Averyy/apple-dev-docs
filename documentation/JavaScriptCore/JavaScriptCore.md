# JavaScriptCore

**Framework**: JavaScriptCore  
**Kind**: module  
**Role**: Framework

Evaluate JavaScript programs from within an app, and support JavaScript scripting of your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Overview

The JavaScriptCore framework provides the ability to evaluate JavaScript programs from within Swift, Objective-C, and C-based apps. You can use also use JavaScriptCore to insert custom objects into the JavaScript environment.

## Topics

### Execution Environment
- [class JSVirtualMachine](./jsvirtualmachine.md)
  A self-contained environment for JavaScript execution.
- [class JSContext](./jscontext.md)
  A JavaScript execution environment.
### JavaScript Code
- [class JSValue](./jsvalue.md)
  A JavaScript value.
- [class JSManagedValue](./jsmanagedvalue.md)
  A JavaScript value with conditional retain behavior to provide automatic memory management.
### Native Code
- [protocol JSExport](./jsexport.md)
  The protocol for exporting Objective-C objects to JavaScript.
### C API
- [C JavaScriptCore API](./c-javascriptcore-api.md)
  Browse the alternative C-based APIs for JavaScriptCore.
### Reference
- [JavaScriptCore Constants](./javascriptcore-constants.md)
### Variables
- [var kJSTypeBigInt: JSType](./kjstypebigint.md)
### Functions
- [func JSBigIntCreateWithDouble(JSContextRef, Double, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef](./jsbigintcreatewithdouble%28_,_,_%29.md)
- [func JSBigIntCreateWithInt64(JSContextRef, Int64, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef](./jsbigintcreatewithint64%28_,_,_%29.md)
- [func JSBigIntCreateWithString(JSContextRef, JSStringRef, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef](./jsbigintcreatewithstring%28_,_,_%29.md)
- [func JSBigIntCreateWithUInt64(JSContextRef, UInt64, UnsafeMutablePointer<JSValueRef?>?) -> JSValueRef](./jsbigintcreatewithuint64%28_,_,_%29.md)
- [func JSValueCompare(JSContextRef, JSValueRef, JSValueRef, UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition](./jsvaluecompare%28_,_,_,_%29.md)
- [func JSValueCompareDouble(JSContextRef, JSValueRef, Double, UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition](./jsvaluecomparedouble%28_,_,_,_%29.md)
- [func JSValueCompareInt64(JSContextRef, JSValueRef, Int64, UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition](./jsvaluecompareint64%28_,_,_,_%29.md)
- [func JSValueCompareUInt64(JSContextRef, JSValueRef, UInt64, UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition](./jsvaluecompareuint64%28_,_,_,_%29.md)
- [func JSValueIsBigInt(JSContextRef, JSValueRef) -> Bool](./jsvalueisbigint%28_,_%29.md)
- [func JSValueToInt32(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef?>?) -> Int32](./jsvaluetoint32%28_,_,_%29.md)
- [func JSValueToInt64(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef?>?) -> Int64](./jsvaluetoint64%28_,_,_%29.md)
- [func JSValueToUInt32(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef?>?) -> UInt32](./jsvaluetouint32%28_,_,_%29.md)
- [func JSValueToUInt64(JSContextRef, JSValueRef, UnsafeMutablePointer<JSValueRef?>?) -> UInt64](./jsvaluetouint64%28_,_,_%29.md)
### Enumerations
- [enum JSRelationCondition](./jsrelationcondition.md)
### Macros
- [JSC_ASSUME_NONNULL_BEGIN](./jsc_assume_nonnull_begin.md)
- [JSC_ASSUME_NONNULL_END](./jsc_assume_nonnull_end.md)
- [JSC_CF_ENUM](./jsc_cf_enum.md)
- [JSC_NONNULL](./jsc_nonnull.md)
- [JSC_NULLABLE](./jsc_nullable.md)
- [JSC_NULL_UNSPECIFIED](./jsc_null_unspecified.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/JavaScriptCore)*