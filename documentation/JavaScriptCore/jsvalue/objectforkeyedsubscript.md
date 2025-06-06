# objectForKeyedSubscript(_:)

**Framework**: JavaScriptCore  
**Kind**: method

Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.

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

The value of the named property, or the JavaScript `undefined` value if no property exists by that name.

#### Discussion

This method is equivalent to the [`forProperty(_:)`](jsvalue/forproperty(_:).md) method, but provides Objective-C subscripting support.

## Parameters

- `key`: The name of a property in the JavaScript object.

## See Also

- [func objectAtIndexedSubscript(Int) -> JSValue!](jsvalue/objectatindexedsubscript(_:).md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func setObject(Any!, atIndexedSubscript: Int)](jsvalue/setobject(_:atindexedsubscript:).md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func setObject(Any!, forKeyedSubscript: Any!)](jsvalue/setobject(_:forkeyedsubscript:).md)
  Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/objectforkeyedsubscript(_:))*