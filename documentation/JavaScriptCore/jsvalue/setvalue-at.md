# setValue(_:at:)

**Framework**: JavaScriptCore  
**Kind**: method

Sets the value at the specified numeric index in the JavaScript object value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Any!, at index: Int)
```

#### Discussion

Calling this method is equivalent to using the subscript operator with a numeric subscript in JavaScript. Use it to access elements of JavaScript arrays or of objects with numerically-indexed properties.

## Parameters

- `value`: The value to set at the specified index.
- `index`: An index in the JavaScript object.

## Topics

### Related Documentation
- [func setObject(Any!, atIndexedSubscript: Int)](jsvalue/setobject(_:atindexedsubscript:).md)
  Sets the value’s JavaScript property at the specified index, allowing subscript syntax.

## See Also

- [func defineProperty(Any!, descriptor: Any!)](jsvalue/defineproperty(_:descriptor:).md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](jsvalue/hasproperty(_:).md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](jsvalue/deleteproperty(_:).md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](jsvalue/atindex(_:).md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](jsvalue/forproperty(_:).md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](jsvalue/setvalue(_:forproperty:).md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/setvalue(_:at:))*