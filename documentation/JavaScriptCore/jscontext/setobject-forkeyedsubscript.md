# setObject(_:forKeyedSubscript:)

**Framework**: JavaScriptCore  
**Kind**: method

Sets the specified JavaScript property of the context’s global object, allowing subscript setter syntax.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setObject(_ object: Any!, forKeyedSubscript key: (any NSCopying & NSObjectProtocol)!)
```

#### Discussion

This method first constructs a [`JSValue`](jsvalue.md) object from the `key` parameter, then uses that value in JavaScript to set the property in the context’s global object.

Use this method (or Objective-C subscript syntax) to bridge native objects or functions for use in JavaScript. For example, the following code creates a JavaScript function whose implementation is an Objective-C block:

```objc
JSContext *context = [[JSContext alloc] init];
context[@"makeNSColor"] = ^(NSDictionary *rgb){
    float r = rgb[@"red"].floatValue;
    float g = rgb[@"green"].floatValue;
    float b = rgb[@"blue"].floatValue;
    return [NSColor colorWithRed:(r / 255.f) green:(g / 255.f) blue:(b / 255.f) alpha:1.0];
};
```

## Parameters

- `object`: The value to set for the JavaScript property.
- `key`: The JavaScript property name to use in the context’s global JavaScript object.

## See Also

- [func objectForKeyedSubscript(Any!) -> JSValue!](jscontext/objectforkeyedsubscript(_:).md)
  Returns the value of the specified JavaScript property in the context’s global object, allowing subscript getter syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/setobject(_:forkeyedsubscript:))*