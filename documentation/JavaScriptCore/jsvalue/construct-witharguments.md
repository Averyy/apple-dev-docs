# construct(withArguments:)

**Framework**: JavaScriptCore  
**Kind**: method

Invokes the value as a JavaScript constructor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func construct(withArguments arguments: [Any]!) -> JSValue!
```

#### Return Value

The result of calling the value as a constructor, or `nil` if the value cannot be treated as a JavaScript constructor.

#### Discussion

Calling a constructor is equivalent to using the `new` keyword in JavaScript.

## Parameters

- `arguments`: The parameters to pass to the constructor. The objects in this array must be other   objects or objects that can be converted to JavaScript values using the methods listed in Creating JavaScript Values.

## See Also

- [func call(withArguments: [Any]!) -> JSValue!](jsvalue/call(witharguments:).md)
  Invokes the value as a JavaScript function.
- [func invokeMethod(String!, withArguments: [Any]!) -> JSValue!](jsvalue/invokemethod(_:witharguments:).md)
  Calls the named JavaScript method on the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/construct(witharguments:))*