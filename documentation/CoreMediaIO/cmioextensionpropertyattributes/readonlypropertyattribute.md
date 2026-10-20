# readOnlyPropertyAttribute

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Type Property

A class property for a read-only property attribute.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class var readOnlyPropertyAttribute: CMIOExtensionPropertyAttributes<AnyObject> { get }
```

```objc
@property (class, readonly) CMIOExtensionPropertyAttributes * readOnlyPropertyAttribute;
```

#### Discussion

The attribute doesn’t contain values for its [`minValue`](./minvalue.md), [`maxValue`](./maxvalue.md), or [`validValues`](./validvalues.md) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes/readonlypropertyattribute)*