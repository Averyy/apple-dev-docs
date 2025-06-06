# attributes

**Framework**: JavaScriptCore  
**Kind**: property

A set of property attributes to give to the property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var attributes: JSPropertyAttributes
```

## See Also

- [var name: UnsafePointer<CChar>!](jsstaticvalue/name.md)
  A null-terminated UTF-8 string that contains the property’s name.
- [var getProperty: JSObjectGetPropertyCallback!](jsstaticvalue/getproperty.md)
  A callback to invoke when getting the property’s value.
- [var setProperty: JSObjectSetPropertyCallback!](jsstaticvalue/setproperty.md)
  A callback to invoke when setting the property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/attributes)*