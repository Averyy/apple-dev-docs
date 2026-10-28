# currentCallee()

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (JSValue *) currentCallee;
```

## Return Value

The currently executing JavaScript function, or `nil` if not within native code called from JavaScript.

## Discussion

Call this method within an Objective-C or Swift block or method invoked from within JavaScript to obtain a [`JSValue`](../jsvalue.md) object representing the JavaScript function responsible for executing that code.

If not currently in code invoked as a callback from JavaScript, this method returns `nil`.

## See Also

### Inspecting callback state in a running context
- [class func current() -> JSContext!](./current%28%29.md)
  Returns the context currently executing JavaScript code.
- [class func currentThis() -> JSValue!](./currentthis%28%29.md)
  Returns the value of the `this` keyword in currently executing JavaScript code.
- [class func currentArguments() -> [Any]!](./currentarguments%28%29.md)
  Returns the arguments to the current native callback from JavaScript code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/currentcallee())*