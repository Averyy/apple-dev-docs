# C JavaScriptCore API

**Framework**: JavaScriptCore

Browse the alternative C-based APIs for JavaScriptCore.

## Topics

### JavaScriptCore Engine Interface
- [typealias JSContextGroupRef](jscontextgroupref.md)
  A group that associates JavaScript contexts with one another.
- [typealias JSContextRef](jscontextref.md)
  A JavaScript execution context.
- [typealias JSGlobalContextRef](jsglobalcontextref.md)
  A global JavaScript execution context.
- [typealias JSStringRef](jsstringref.md)
  A UTF-16 character buffer.
- [typealias JSClassRef](jsclassref.md)
  A JavaScript class.
### JavaScript Data Types
- [typealias JSValueRef](jsvalueref.md)
  A JavaScript value.
- [typealias JSObjectRef](jsobjectref.md)
  A JavaScript object.
### Script Evaluation
- [func JSCheckScriptSyntax(JSContextRef!, JSStringRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jscheckscriptsyntax(_:_:_:_:_:).md)
  Checks for syntax errors in a string of JavaScript.
- [func JSEvaluateScript(JSContextRef!, JSStringRef!, JSObjectRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsevaluatescript(_:_:_:_:_:_:).md)
  Evaluates a string of JavaScript.
- [func JSGarbageCollect(JSContextRef!)](jsgarbagecollect(_:).md)
  Performs a JavaScript garbage collection.
### Constants
- [var JSC_OBJC_API_ENABLED: Int32](jsc_objc_api_enabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/c-javascriptcore-api)*