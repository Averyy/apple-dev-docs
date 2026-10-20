# minValue

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The minimum value a property supports.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
@NSCopying
var minValue: ObjectType? { get }
```

```objc
@property (atomic, copy, readonly, nullable) ObjectType minValue;
```

## See Also

### Inspecting Attributes
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether a property is read-only.
- [var maxValue: ObjectType?](./maxvalue.md)
  The maximum value a property supports.
- [var validValues: [ObjectType]?](./validvalues.md)
  An array of discrete values that this property supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes/minvalue)*