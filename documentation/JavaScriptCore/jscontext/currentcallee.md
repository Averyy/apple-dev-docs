# currentCallee()

**Framework**: JavaScriptCore  
**Kind**: method

Returns the currently executing JavaScript function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func currentCallee() -> JSValue!
```

#### Return Value

The currently executing JavaScript function, or `nil` if not within native code called from JavaScript.

#### Discussion

Call this method within an Objective-C or Swift block or method invoked from within JavaScript to obtain a [`JSValue`](jsvalue.md) object representing the JavaScript function responsible for executing that code.

If not currently in code invoked as a callback from JavaScript, this method returns `nil`.

## See Also

- [class func current() -> JSContext!](jscontext/current.md)
  Returns the context currently executing JavaScript code.
- [class func currentThis() -> JSValue!](jscontext/currentthis.md)
  Returns the value of the `this` keyword in currently executing JavaScript code.
- [class func currentArguments() -> [Any]!](jscontext/currentarguments.md)
  Returns the arguments to the current native callback from JavaScript code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/currentcallee())*