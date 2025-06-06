# invokeMethod(_:withArguments:)

**Framework**: JavaScriptCore  
**Kind**: method

Calls the named JavaScript method on the value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func invokeMethod(_ method: String!, withArguments arguments: [Any]!) -> JSValue!
```

#### Return Value

The result of calling the value as a constructor, or `nil` if the value cannot be treated as a JavaScript constructor.

#### Discussion

Calling this Objective-C method first uses the [`forProperty(_:)`](jsvalue/forproperty(_:).md) method to look up the named field of the JavaScript value. Then, JavaScriptCore treats that field’s contents as a JavaScript function and sets the JavaScript `this` keyword to refer to this [`JSValue`](jsvalue.md) instance.

## Parameters

- `method`: The name of a method on the value; that is, of a field whose contents are a function value.
- `arguments`: The parameters to pass to the method. The objects in this array must be other   objects or objects that can be converted to JavaScript values using the methods listed in the Creating JavaScript Values section in  .

## See Also

- [func call(withArguments: [Any]!) -> JSValue!](jsvalue/call(witharguments:).md)
  Invokes the value as a JavaScript function.
- [func construct(withArguments: [Any]!) -> JSValue!](jsvalue/construct(witharguments:).md)
  Invokes the value as a JavaScript constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/invokemethod(_:witharguments:))*