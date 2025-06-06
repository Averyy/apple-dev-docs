# JSEvaluateScript(_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Evaluates a string of JavaScript.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSEvaluateScript(_ ctx: JSContextRef!, _ script: JSStringRef!, _ thisObject: JSObjectRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!
```

#### Return Value

The value that results from evaluating `script`, or `NULL` if the system throws an exception.

## Parameters

- `ctx`: The execution context to use.
- `script`: A   that contains the script to evaluate.
- `thisObject`: The object to use as   or   to use the global object as  .
- `sourceURL`: A   that contains a URL for the script’s source file. The system only uses this when reporting exceptions. Pass   to omit source file information in exceptions.
- `startingLineNumber`: An integer value that specifies the script’s starting line number in the file at  . The system only uses this when reporting exceptions.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSCheckScriptSyntax(JSContextRef!, JSStringRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jscheckscriptsyntax(_:_:_:_:_:).md)
  Checks for syntax errors in a string of JavaScript.
- [func JSGarbageCollect(JSContextRef!)](jsgarbagecollect(_:).md)
  Performs a JavaScript garbage collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsevaluatescript(_:_:_:_:_:_:))*