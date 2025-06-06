# setObject(_:forKeyedSubscript:)

**Framework**: JavaScriptCore  
**Kind**: method

Sets the value’s JavaScript property named with the specified key, allowing subscript syntax.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setObject(_ object: Any!, forKeyedSubscript key: Any!)
```

#### Discussion

This method is equivalent to the [`setValue(_:forProperty:)`](jsvalue/setvalue(_:forproperty:).md) method, but provides Objective-C subscripting support.

## Parameters

- `object`: The value to set for the named JavaScript property.
- `key`: The name of a property in the JavaScript object.

## See Also

- [func objectAtIndexedSubscript(Int) -> JSValue!](jsvalue/objectatindexedsubscript(_:).md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func setObject(Any!, atIndexedSubscript: Int)](jsvalue/setobject(_:atindexedsubscript:).md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.
- [func objectForKeyedSubscript(Any!) -> JSValue!](jsvalue/objectforkeyedsubscript(_:).md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/setobject(_:forkeyedsubscript:))*