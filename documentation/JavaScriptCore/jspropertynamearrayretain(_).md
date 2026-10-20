# JSPropertyNameArrayRetain(_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

Retains a JavaScript property name array.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSPropertyNameArrayRetain(_ array: JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!
```

```c
JSPropertyNameArrayRefJSPropertyNameArrayRetain(JSPropertyNameArrayRef array);
```

#### Return Value

A [`JSPropertyNameArrayRef`](./jspropertynamearrayref.md) that is the same as `array`.

## Parameters

- `array`: The [`JSPropertyNameArrayRef`](./jspropertynamearrayref.md) to retain.

## See Also

### Working with Properties
- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](./jspropertynameaccumulatoraddname%28_,_%29.md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetCount(JSPropertyNameArrayRef!) -> Int](./jspropertynamearraygetcount%28_%29.md)
  Gets a count of the number of items in a JavaScript property name array.
- [func JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef!, Int) -> JSStringRef!](./jspropertynamearraygetnameatindex%28_,_%29.md)
  Gets a property name at a specified index in a JavaScript property name array.
- [func JSPropertyNameArrayRelease(JSPropertyNameArrayRef!)](./jspropertynamearrayrelease%28_%29.md)
  Releases a JavaScript property name array.
- [typealias JSPropertyAttributes](./jspropertyattributes.md)
  A set of JavaScript property attributes.
- [JSPropertyAttribute](./jspropertyattribute.md)
  A JavaScript property attribute.
- [typealias JSPropertyNameArrayRef](./jspropertynamearrayref.md)
  An array of JavaScript property names.
- [typealias JSPropertyNameAccumulatorRef](./jspropertynameaccumulatorref.md)
  An ordered set of the names of a JavaScript object’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jspropertynamearrayretain(_:))*