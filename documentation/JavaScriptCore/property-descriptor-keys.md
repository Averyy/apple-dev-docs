# Property Descriptor Keys

**Framework**: JavaScriptCore

Keys for the native dictionary representation of a JavaScript property descriptor, used with the [`defineProperty(_:descriptor:)`](jsvalue/defineproperty(_:descriptor:).md) method.

## Topics

### Constants
- [let JSPropertyDescriptorWritableKey: String](jspropertydescriptorwritablekey.md)
  The Boolean value for this key determines whether the property permits assignment with the JavaScript `=` operator.
- [let JSPropertyDescriptorEnumerableKey: String](jspropertydescriptorenumerablekey.md)
  The Boolean value for this key determines whether the property appears when enumerating the JavaScript object’s properties.
- [let JSPropertyDescriptorConfigurableKey: String](jspropertydescriptorconfigurablekey.md)
  The Boolean value for this key determines whether the property deleted from its JavaScript object or its descriptor changed.
- [let JSPropertyDescriptorValueKey: String](jspropertydescriptorvaluekey.md)
  The value for the property on the JavaScript object.
- [let JSPropertyDescriptorGetKey: String](jspropertydescriptorgetkey.md)
  The JavaScript function to be invoked when reading the property.
- [let JSPropertyDescriptorSetKey: String](jspropertydescriptorsetkey.md)
  The JavaScript function to be invoked when writing to the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/property-descriptor-keys)*