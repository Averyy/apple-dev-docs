# atIndex(_:)

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Instance Method

Returns the value at the specified numeric index in the JavaScript object value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func atIndex(_ index: Int) -> JSValue!
```

```objc
- (JSValue *) valueAtIndex:(NSUInteger) index;
```

## Return Value

The value at the specified index, or the JavaScript `undefined` value if no property exists at that index.

## Discussion

Calling this method is equivalent to using the subscript operator with a numeric subscript in JavaScript. Use it to access elements of JavaScript arrays or of objects with numerically-indexed properties.

## Parameters

- `index`: An index in the JavaScript object.

## Topics

### Related Documentation
- [func objectAtIndexedSubscript(Int) -> JSValue!](./objectatindexedsubscript%28_%29.md)
  Returns the value’s JavaScript property at the specified index, allowing subscript syntax.

## See Also

### Working with Container Values
- [func defineProperty(Any!, descriptor: Any!)](./defineproperty%28_,descriptor%29.md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](./hasproperty%28_%29.md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](./deleteproperty%28_%29.md)
  Deletes the named property from the JavaScript object value.
- [func setValue(Any!, at: Int)](./setvalue%28_,at%29.md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](./forproperty%28_%29.md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](./setvalue%28_,forproperty%29.md)
  Sets the value of the named property in the JavaScript object value.
- [typealias JSValueProperty](../jsvalueproperty.md)
  A type that identifies a property of a JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/atindex(_:))*