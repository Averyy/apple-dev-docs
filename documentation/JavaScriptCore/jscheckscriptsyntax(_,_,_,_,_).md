# JSCheckScriptSyntax(_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Checks for syntax errors in a string of JavaScript.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSCheckScriptSyntax(_ ctx: JSContextRef!, _ script: JSStringRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> Bool
```

```c
bool JSCheckScriptSyntax(JSContextRef ctx, JSStringRef script, JSStringRef sourceURL, int startingLineNumber, JSValueRef*exception);
```

#### Return Value

[`true`](../Swift/true.md) if the script is syntactically correct; otherwise, [`false`](../Swift/false.md).

## Parameters

- `ctx`: The execution context to use.
- `script`: A [`JSStringRef`](./jsstringref.md) that contains the script to check for syntax errors.
- `sourceURL`: A [`JSStringRef`](./jsstringref.md) that contains a URL for the script’s source file. The system only uses this when reporting exceptions. Pass `NULL` to omit source file information in exceptions.
- `startingLineNumber`: An integer value that specifies the script’s starting line number in the file at `sourceURL`. The system only uses this when reporting exceptions.
- `exception`: A pointer to a [`JSValueRef`](./jsvalueref.md) to store a syntax error exception in, if any. Pass `NULL` to ignore any syntax error exception.

## See Also

### Script Evaluation
- [func JSEvaluateScript(JSContextRef!, JSStringRef!, JSObjectRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](./jsevaluatescript%28_,_,_,_,_,_%29.md)
  Evaluates a string of JavaScript.
- [func JSGarbageCollect(JSContextRef!)](./jsgarbagecollect%28_%29.md)
  Performs a JavaScript garbage collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscheckscriptsyntax(_:_:_:_:_:))*