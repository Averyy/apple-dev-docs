# aeDesc

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The `AEDesc` structure encapsulated by the receiver, if it has one.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var aeDesc: UnsafePointer<AEDesc>? { get }
```

```objc
@property (readonly, nullable) const AEDesc * aeDesc;
```

## Discussion

If the receiver has a valid `AEDesc` structure, returns a pointer to it; otherwise returns `nil`.

## See Also

### Getting Information About a Descriptor
- [var booleanValue: Bool](./booleanvalue.md)
  The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.
- [func coerce(toDescriptorType: DescType) -> NSAppleEventDescriptor?](./coerce%28todescriptortype%29.md)
  Returns a descriptor obtained by coercing the receiver to the specified type.
- [var data: Data](./data.md)
  The receiver’s data.
- [var descriptorType: DescType](./descriptortype.md)
  The descriptor type of the receiver.
- [var enumCodeValue: OSType](./enumcodevalue.md)
  The contents of the receiver as an enumeration type, coercing to `typeEnumerated` if necessary.
- [var int32Value: Int32](./int32value.md)
  The contents of the receiver as an integer, coercing (to `typeSInt32`) if necessary.
- [var numberOfItems: Int](./numberofitems.md)
  The number of descriptors in the receiver’s descriptor list.
- [var stringValue: String?](./stringvalue.md)
  The contents of the receiver as a Unicode text string, coercing to `typeUnicodeText` if necessary.
- [var typeCodeValue: OSType](./typecodevalue.md)
  The contents of the receiver as a type, coercing to `typeType` if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/aedesc)*