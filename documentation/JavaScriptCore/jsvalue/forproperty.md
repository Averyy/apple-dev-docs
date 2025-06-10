# forProperty(_:)

**Framework**: JavaScriptCore  
**Kind**: method

Returns the value of the named property in the JavaScript object value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func forProperty(_ property: String!) -> JSValue!
```

#### Return Value

The value of the named property, or the JavaScript `undefined` value if no property exists by that name.

#### Discussion

Calling this method is equivalent to using the subscript operator with a string subscript in JavaScript. Use it to access fields or properties in JavaScript objects.

## Parameters

- `property`: The name of a property in the JavaScript object.

## Topics

### Related Documentation
- [func objectForKeyedSubscript(Any!) -> JSValue!](jsvalue/objectforkeyedsubscript(_:).md)
  Returns the value’s JavaScript property named with the specified key, allowing subscript syntax.

## See Also

- [func defineProperty(Any!, descriptor: Any!)](jsvalue/defineproperty(_:descriptor:).md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](jsvalue/hasproperty(_:).md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](jsvalue/deleteproperty(_:).md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](jsvalue/atindex(_:).md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](jsvalue/setvalue(_:at:).md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](jsvalue/setvalue(_:forproperty:).md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/forproperty(_:))*