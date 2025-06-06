# name

**Framework**: JavaScriptCore  
**Kind**: property

A null-terminated UTF-8 string that contains the property’s name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: UnsafePointer<CChar>!
```

## See Also

- [var getProperty: JSObjectGetPropertyCallback!](jsstaticvalue/getproperty.md)
  A callback to invoke when getting the property’s value.
- [var setProperty: JSObjectSetPropertyCallback!](jsstaticvalue/setproperty.md)
  A callback to invoke when setting the property’s value.
- [var attributes: JSPropertyAttributes](jsstaticvalue/attributes.md)
  A set of property attributes to give to the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstaticvalue/name)*