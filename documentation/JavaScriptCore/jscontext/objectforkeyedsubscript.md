# objectForKeyedSubscript(_:)

**Framework**: JavaScriptCore  
**Kind**: method

Returns the value of the specified JavaScript property in the context’s global object, allowing subscript getter syntax.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func objectForKeyedSubscript(_ key: Any!) -> JSValue!
```

#### Return Value

The JavaScript property named by `key`, or `nil` if no such field or function exists.

#### Discussion

This method first constructs a [`JSValue`](jsvalue.md) object from the `key` parameter, then uses that value in JavaScript to look up the name of a property in the context’s global object.

## Parameters

- `key`: The name of a JavaScript property in the context’s global JavaScript object.

## See Also

- [func setObject(Any!, forKeyedSubscript: (any NSCopying & NSObjectProtocol)!)](jscontext/setobject(_:forkeyedsubscript:).md)
  Sets the specified JavaScript property of the context’s global object, allowing subscript setter syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/objectforkeyedsubscript(_:))*