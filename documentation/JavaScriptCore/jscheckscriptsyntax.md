# JSCheckScriptSyntax(_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the script is syntactically correct; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `ctx`: The execution context to use.
- `script`: A   that contains the script to check for syntax errors.
- `sourceURL`: A   that contains a URL for the script’s source file. The system only uses this when reporting exceptions. Pass   to omit source file information in exceptions.
- `startingLineNumber`: An integer value that specifies the script’s starting line number in the file at  . The system only uses this when reporting exceptions.
- `exception`: A pointer to a   to store a syntax error exception in, if any. Pass   to ignore any syntax error exception.

## See Also

- [func JSEvaluateScript(JSContextRef!, JSStringRef!, JSObjectRef!, JSStringRef!, Int32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsevaluatescript(_:_:_:_:_:_:).md)
  Evaluates a string of JavaScript.
- [func JSGarbageCollect(JSContextRef!)](jsgarbagecollect(_:).md)
  Performs a JavaScript garbage collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscheckscriptsyntax(_:_:_:_:_:))*