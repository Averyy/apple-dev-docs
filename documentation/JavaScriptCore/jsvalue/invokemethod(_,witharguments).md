# invokeMethod(_:withArguments:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (JSValue *) invokeMethod:(NSString *) method withArguments:(NSArray *) arguments;
```

## Return Value

The result of calling the value as a constructor, or `nil` if the value cannot be treated as a JavaScript constructor.

## Discussion

Calling this Objective-C method first uses the [`forProperty(_:)`](./forproperty%28_%29.md) method to look up the named field of the JavaScript value. Then, JavaScriptCore treats that field’s contents as a JavaScript function and sets the JavaScript `this` keyword to refer to this [`JSValue`](../jsvalue.md) instance.

## Parameters

- `method`: The name of a method on the value; that is, of a field whose contents are a function value.
- `arguments`: The parameters to pass to the method. The objects in this array must be other [`JSValue`](../jsvalue.md) objects or objects that can be converted to JavaScript values using the methods listed in the Creating JavaScript Values section in [`JSValue`](../jsvalue.md).

## See Also

### Working with Function and Constructor Values
- [func call(withArguments: [Any]!) -> JSValue!](./call%28witharguments%29.md)
  Invokes the value as a JavaScript function.
- [func construct(withArguments: [Any]!) -> JSValue!](./construct%28witharguments%29.md)
  Invokes the value as a JavaScript constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/invokemethod(_:witharguments:))*