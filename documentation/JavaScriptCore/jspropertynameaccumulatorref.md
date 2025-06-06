# JSPropertyNameAccumulatorRef

**Framework**: JavaScriptCore  
**Kind**: typealias

An ordered set of the names of a JavaScript object’s properties.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias JSPropertyNameAccumulatorRef = OpaquePointer
```

## See Also

- [func JSPropertyNameAccumulatorAddName(JSPropertyNameAccumulatorRef!, JSStringRef!)](jspropertynameaccumulatoraddname(_:_:).md)
  Adds a property name to a JavaScript property name accumulator.
- [func JSPropertyNameArrayGetCount(JSPropertyNameArrayRef!) -> Int](jspropertynamearraygetcount(_:).md)
  Gets a count of the number of items in a JavaScript property name array.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jspropertynameaccumulatorref)*