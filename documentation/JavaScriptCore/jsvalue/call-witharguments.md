# call(withArguments:)

**Framework**: JavaScriptCore  
**Kind**: method

Invokes the value as a JavaScript function.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func call(withArguments arguments: [Any]!) -> JSValue!
```

#### Return Value

The result of calling the value as a function, or `nil` if the value cannot be treated as a JavaScript function.

#### Discussion

In JavaScript, if a function does not explicitly return a value, it implicitly returns the value `undefined`—use the [`isUndefined`](jsvalue/isundefined.md) property to test for this result.

## Parameters

- `arguments`: The parameters to pass to the function. The objects in this array must be other   objects or objects that can be converted to JavaScript values using the methods listed in the Creating JavaScript Values section in  .

## See Also

- [func construct(withArguments: [Any]!) -> JSValue!](jsvalue/construct(witharguments:).md)
  Invokes the value as a JavaScript constructor.
- [func invokeMethod(String!, withArguments: [Any]!) -> JSValue!](jsvalue/invokemethod(_:witharguments:).md)
  Calls the named JavaScript method on the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/call(witharguments:))*