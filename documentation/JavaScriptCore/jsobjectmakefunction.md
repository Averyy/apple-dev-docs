# JSObjectMakeFunction(_:_:_:_:_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Creates a function with a specified script as its body.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSObjectMakeFunction(_ ctx: JSContextRef!, _ name: JSStringRef!, _ parameterCount: UInt32, _ parameterNames: UnsafePointer<JSStringRef?>!, _ body: JSStringRef!, _ sourceURL: JSStringRef!, _ startingLineNumber: Int32, _ exception: UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!
```

#### Return Value

A [`JSObjectRef`](jsobjectref.md) that is a function, or `NULL` if either `body` or `parameterNames` contains a syntax error. The object’s prototype is the default function prototype.

#### Discussion

Use this method when you want to execute a script repeatedly to avoid the cost of reparsing the script before each execution.

## Parameters

- `ctx`: The execution context to use.
- `name`: A   that contains the function’s name. The system uses this when converting the function to a string. Pass   to create an anonymous function.
- `parameterCount`: An integer count of the number of parameter names in  .
- `parameterNames`: A   array that contains the names of the function’s parameters. Pass   if   is  .
- `body`: A   that contains the script to use as the function’s body.
- `sourceURL`: A   that contains a URL for the script’s source file. The system only uses this when reporting exceptions. Pass   if you don’t want to include source file information in exceptions.
- `startingLineNumber`: An integer value that specifies the script’s starting line number in the file at  . The system only uses this when reporting exceptions.
- `exception`: A pointer to a   to store an exception in, if any. Pass   to discard any exception.

## See Also

- [func JSObjectCallAsConstructor(JSContextRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectcallasconstructor(_:_:_:_:_:).md)
  Calls an object as a constructor.
- [func JSObjectCallAsFunction(JSContextRef!, JSObjectRef!, JSObjectRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectcallasfunction(_:_:_:_:_:_:).md)
  Calls an object as a function.
- [func JSObjectCopyPropertyNames(JSContextRef!, JSObjectRef!) -> JSPropertyNameArrayRef!](jsobjectcopypropertynames(_:_:).md)
  Gets the names of an object’s enumerable properties.
- [func JSObjectDeleteProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> Bool](jsobjectdeleteproperty(_:_:_:_:).md)
  Deletes a property from an object.
- [func JSObjectGetPrivate(JSObjectRef!) -> UnsafeMutableRawPointer!](jsobjectgetprivate(_:).md)
  Gets an object’s private data.
- [func JSObjectGetProperty(JSContextRef!, JSObjectRef!, JSStringRef!, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectgetproperty(_:_:_:_:).md)
  Gets a property from an object.
- [func JSObjectGetPropertyAtIndex(JSContextRef!, JSObjectRef!, UInt32, UnsafeMutablePointer<JSValueRef?>!) -> JSValueRef!](jsobjectgetpropertyatindex(_:_:_:_:).md)
  Gets a property from an object by numeric index.
- [func JSObjectGetPrototype(JSContextRef!, JSObjectRef!) -> JSValueRef!](jsobjectgetprototype(_:_:).md)
  Gets an object’s prototype.
- [func JSObjectHasProperty(JSContextRef!, JSObjectRef!, JSStringRef!) -> Bool](jsobjecthasproperty(_:_:_:).md)
  Tests whether an object has a specified property.
- [func JSObjectIsConstructor(JSContextRef!, JSObjectRef!) -> Bool](jsobjectisconstructor(_:_:).md)
  Tests whether you can call an object as a constructor.
- [func JSObjectIsFunction(JSContextRef!, JSObjectRef!) -> Bool](jsobjectisfunction(_:_:).md)
  Tests whether you can call an object as a function.
- [func JSObjectMake(JSContextRef!, JSClassRef!, UnsafeMutableRawPointer!) -> JSObjectRef!](jsobjectmake(_:_:_:).md)
  Creates a JavaScript object.
- [func JSObjectMakeArray(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakearray(_:_:_:_:).md)
  Creates a JavaScript array object.
- [func JSObjectMakeConstructor(JSContextRef!, JSClassRef!, JSObjectCallAsConstructorCallback!) -> JSObjectRef!](jsobjectmakeconstructor(_:_:_:).md)
  Creates a JavaScript constructor.
- [func JSObjectMakeDate(JSContextRef!, Int, UnsafePointer<JSValueRef?>!, UnsafeMutablePointer<JSValueRef?>!) -> JSObjectRef!](jsobjectmakedate(_:_:_:_:).md)
  Creates a JavaScript date object as though invoking the built-in date constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsobjectmakefunction(_:_:_:_:_:_:_:_:))*