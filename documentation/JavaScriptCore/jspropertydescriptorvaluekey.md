# JSPropertyDescriptorValueKey

**Framework**: JavaScriptCore  
**Kind**: var

The value for the property on the JavaScript object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let JSPropertyDescriptorValueKey: String
```

## See Also

- [let JSPropertyDescriptorWritableKey: String](jspropertydescriptorwritablekey.md)
  The Boolean value for this key determines whether the property permits assignment with the JavaScript `=` operator.
- [let JSPropertyDescriptorEnumerableKey: String](jspropertydescriptorenumerablekey.md)
  The Boolean value for this key determines whether the property appears when enumerating the JavaScript object’s properties.
- [let JSPropertyDescriptorConfigurableKey: String](jspropertydescriptorconfigurablekey.md)
  The Boolean value for this key determines whether the property deleted from its JavaScript object or its descriptor changed.
- [let JSPropertyDescriptorGetKey: String](jspropertydescriptorgetkey.md)
  The JavaScript function to be invoked when reading the property.
- [let JSPropertyDescriptorSetKey: String](jspropertydescriptorsetkey.md)
  The JavaScript function to be invoked when writing to the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jspropertydescriptorvaluekey)*