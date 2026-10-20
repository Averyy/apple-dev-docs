# validValues

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An array of discrete values that this property supports.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var validValues: [ObjectType]? { get }
```

```objc
@property (atomic, copy, readonly, nullable) NSArray<id> * validValues;
```

## See Also

### Inspecting Attributes
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether a property is read-only.
- [var minValue: ObjectType?](./minvalue.md)
  The minimum value a property supports.
- [var maxValue: ObjectType?](./maxvalue.md)
  The maximum value a property supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes/validvalues)*