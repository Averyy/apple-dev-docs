# JSGarbageCollect(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Performs a JavaScript garbage collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSGarbageCollect(_ ctx: JSContextRef!)
```

```c
void JSGarbageCollect(JSContextRef ctx);
```

#### Discussion

The system doesn’t collect JavaScript values that are on the machine stack, are in a register, are receiving protection from [`JSValueProtect(_:_:)`](./jsvalueprotect%28_,_%29.md), are the global object of an execution context, or are reachable from any such value.

During JavaScript execution, you don’t have to call this function because the JavaScript engine collects garbage as necessary. The system automatically destroys JavaScript values within a context group when the last reference to the context group releases.

## Parameters

- `ctx`: The execution context to use.

## See Also

### Script Evaluation
- [func JSCheckScriptSyntax(JSContextRef!, JSStringRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> Bool](./jscheckscriptsyntax%28_,_,_,_,_%29.md)
  Checks for syntax errors in a string of JavaScript.
- [func JSEvaluateScript(JSContextRef!, JSStringRef!, JSObjectRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsevaluatescript%28_,_,_,_,_,_%29.md)
  Evaluates a string of JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsgarbagecollect(_:))*