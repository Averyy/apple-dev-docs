# JSValueProperty

**Framework**: JavaScriptCore  
**Kind**: typealias  
**Role**: Type Alias

A type that identifies a property of a JavaScript value.

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
typealias JSValueProperty = AnyObject
```

*tvOS*

```swift
typealias JSValueProperty = NSString
```

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```c
typedef id JSValueProperty;
```

*tvOS*

```c
typedef NSString * JSValueProperty;
```

## See Also

### Working with Container Values
- [func defineProperty(Any!, descriptor: Any!)](./jsvalue/defineproperty%28_,descriptor%29.md)
  Defines a property on the JavaScript object value or modifies a property’s definition.
- [func hasProperty(Any!) -> Bool](./jsvalue/hasproperty%28_%29.md)
  Returns a Boolean value indicating whether the JavaScript value has a defined property with the specified name.
- [func deleteProperty(Any!) -> Bool](./jsvalue/deleteproperty%28_%29.md)
  Deletes the named property from the JavaScript object value.
- [func atIndex(Int) -> JSValue!](./jsvalue/atindex%28_%29.md)
  Returns the value at the specified numeric index in the JavaScript object value.
- [func setValue(Any!, at: Int)](./jsvalue/setvalue%28_,at%29.md)
  Sets the value at the specified numeric index in the JavaScript object value.
- [func forProperty(Any!) -> JSValue!](./jsvalue/forproperty%28_%29.md)
  Returns the value of the named property in the JavaScript object value.
- [func setValue(Any!, forProperty: Any!)](./jsvalue/setvalue%28_,forproperty%29.md)
  Sets the value of the named property in the JavaScript object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueproperty)*