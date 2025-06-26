# defineProperty(_:descriptor:)

**Framework**: JavaScriptCore  
**Kind**: method

Defines a property on the JavaScript object value or modifies a property’s definition.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func defineProperty(_ property: String!, descriptor: Any!)
```

#### Discussion

Calling this method is equivalent to using the `Object.defineProperty` method in JavaScript. The `descriptor` parameter has the same format required by that JavaScript method; for convenience when calling from Objective-C or Swift, you can also construct it as a dictionary with the keys listed in [`Property Descriptor Keys`](property-descriptor-keys.md).

The descriptor determines the behavior of the JavaScript property, and must fit one of three cases:

- Data Descriptor: Contains one or both of the keys `value` and `writable`, and optionally also contains the keys `enumerable` or `configurable`. Cannot contain the keys `get` or `set`. Use a data descriptor to create or modify the attributes of a data property on an object (replacing any existing accessor property).
- Accessor Descriptor: Contains one or both of the keys `get` or `set`, and optionally also contains the keys `enumerable` or `configurable`. Cannot contain the keys `value` and `writable`. Use an accessor descriptor to create or modify the attributes of an accessor property on an object (replacing any existing data property).
- Generic Descriptor: Contains one or both of the keys `enumerable` or `configurable`, and cannot contain any other keys. Use a genetic descriptor to modify the attributes of an existing data or accessor property, or to create a new data property.

## Parameters

- `property`: The name of the property to define or modify.
- `descriptor`: A JavaScript object whose keys and values define the property’s behavior.

## See Also

- [func hasProperty(Any!) -> Bool](jsvalue/hasproperty(_:).md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](jsvalue/deleteproperty(_:).md)
  Deletes the named property from the JavaScript object value.
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

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/defineproperty(_:descriptor:))*