# callAsFunction

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

A callback to invoke when calling the property as a function.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var callAsFunction: JSObjectCallAsFunctionCallback!
```

```c
JSObjectCallAsFunctionCallback callAsFunction;
```

## See Also

### Accessing Static Function Information
- [var name: UnsafePointer<CChar>!](./name.md)
  A null-terminated UTF-8 string that contains the property’s name.
- [var attributes: JSPropertyAttributes](./attributes.md)
  A set of property attributes to give to the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstaticfunction/callasfunction)*