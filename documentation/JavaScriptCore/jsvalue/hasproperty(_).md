# hasProperty(_:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
func hasProperty(_ property: Any!) -> Bool
```

*tvOS*

```swift
func hasProperty(_ property: String!) -> Bool
```

```objc
- (BOOL) hasProperty:(JSValueProperty) property;
```

## Return Value

[`true`](../../Swift/true.md) if the JavaScript object has a defined property by that name; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `property`: The name of a property to query for in the JavaScript object value.

## See Also

### Working with Container Values
- [func defineProperty(Any!, descriptor: Any!)](./defineproperty%28_,descriptor%29.md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func deleteProperty(Any!) -> Bool](./deleteproperty%28_%29.md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](./atindex%28_%29.md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](./setvalue%28_,at%29.md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](./forproperty%28_%29.md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](./setvalue%28_,forproperty%29.md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](../jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/hasproperty(_:))*