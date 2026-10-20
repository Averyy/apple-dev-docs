# isReadOnly

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a property is read-only.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var isReadOnly: Bool { get }
```

```objc
@property (atomic, readonly, getter=isReadOnly) BOOL readOnly;
```

## See Also

### Inspecting Attributes
- [var minValue: ObjectType?](./minvalue.md)
  The minimum value a property supports.
- [var maxValue: ObjectType?](./maxvalue.md)
  The maximum value a property supports.
- [var validValues: [ObjectType]?](./validvalues.md)
  An array of discrete values that this property supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes/isreadonly)*