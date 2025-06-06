# deleteProperty(_:)

**Framework**: JavaScriptCore  
**Kind**: method

Deletes the named property from the JavaScript object value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func deleteProperty(_ property: Any!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if property deletion was successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Calling this method is equivalent to using the JavaScript `delete` operator on an object (for example, `delete object.property`). After deletion, attempting to retrieve the property’s value results in the undefined value, and any descriptor information that defines the property’s behavior (see the [`defineProperty(_:descriptor:)`](jsvalue/defineproperty(_:descriptor:).md) method or the JavaScript `defineProperty` function) is lost.

## Parameters

- `property`: The name of a property in the JavaScript object value.

## See Also

- [func defineProperty(Any!, descriptor: Any!)](jsvalue/defineproperty(_:descriptor:).md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](jsvalue/hasproperty(_:).md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func atIndex(Int) -> JSValue!](jsvalue/atindex(_:).md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](jsvalue/setvalue(_:at:).md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](jsvalue/forproperty(_:).md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](jsvalue/setvalue(_:forproperty:).md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/deleteproperty(_:))*