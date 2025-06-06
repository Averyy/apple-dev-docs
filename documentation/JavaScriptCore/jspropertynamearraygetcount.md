# JSPropertyNameArrayGetCount(_:)

**Framework**: JavaScriptCore  
**Kind**: func

Gets a count of the number of items in a JavaScript property name array.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSPropertyNameArrayGetCount(_ array: JSPropertyNameArrayRef!) -> Int
```

#### Return Value

An integer count of the number of names in `array`.

## Parameters

- `array`: The array to retrieve the count from.

## See Also

- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](jspropertynameaccumulatoraddname(_:_:).md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetNameAtIndex(JSPropertyNameArrayRef!, Int) -> JSStringRef!](jspropertynamearraygetnameatindex(_:_:).md)
  Gets a property name at a specified index in a JavaScript property name array.
- [func JSPropertyNameArrayRelease(JSPropertyNameArrayRef!)](jspropertynamearrayrelease(_:).md)
  Releases a JavaScript property name array.
- [func JSPropertyNameArrayRetain(JSPropertyNameArrayRef!) -> JSPropertyNameArrayRef!](jspropertynamearrayretain(_:).md)
  Retains a JavaScript property name array.
- [typealias JSPropertyAttributes](jspropertyattributes.md)
  A set of JavaScript property attributes.
- [JSPropertyAttribute](jspropertyattribute.md)
  A JavaScript property attribute.
- [typealias JSPropertyNameArrayRef](jspropertynamearrayref.md)
  An array of JavaScript property names.
- [typealias JSPropertyNameAccumulatorRef](jspropertynameaccumulatorref.md)
  An ordered set of the names of a JavaScript object’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jspropertynamearraygetcount(_:))*