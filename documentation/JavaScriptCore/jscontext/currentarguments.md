# currentArguments()

**Framework**: JavaScriptCore  
**Kind**: method

Returns the arguments to the current native callback from JavaScript code.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func currentArguments() -> [Any]!
```

#### Return Value

The current callback arguments, or `nil` if not within native code called from JavaScript.

#### Discussion

Call this method within an Objective-C or Swift block or method invoked from within JavaScript to obtain an array of [`JSValue`](jsvalue.md) objects representing the arguments to the JavaScript function responsible for that callback.

If not currently in code invoked as a callback from JavaScript, this method returns `nil`.

## See Also

- [class func current() -> JSContext!](jscontext/current.md)
  Returns the context currently executing JavaScript code.
- [class func currentCallee() -> JSValue!](jscontext/currentcallee.md)
  Returns the currently executing JavaScript function.
- [class func currentThis() -> JSValue!](jscontext/currentthis.md)
  Returns the value of the `this` keyword in currently executing JavaScript code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/currentarguments())*