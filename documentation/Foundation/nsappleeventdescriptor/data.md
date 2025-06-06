# data

**Framework**: Foundation  
**Kind**: property

The receiver’s data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var data: Data { get }
```

#### Discussion

An instance of `NSData` containing the receiver’s data, or `nil` if an error occurs.

## See Also

- [var aeDesc: UnsafePointer<AEDesc>?](nsappleeventdescriptor/aedesc.md)
  The `AEDesc` structure encapsulated by the receiver, if it has one.
- [var booleanValue: Bool](nsappleeventdescriptor/booleanvalue.md)
  The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.
- [func coerce(toDescriptorType: DescType) -> NSAppleEventDescriptor?](nsappleeventdescriptor/coerce(todescriptortype:).md)
  Returns a descriptor obtained by coercing the receiver to the specified type.
- [var descriptorType: DescType](nsappleeventdescriptor/descriptortype.md)
  The descriptor type of the receiver.
- [var enumCodeValue: OSType](nsappleeventdescriptor/enumcodevalue.md)
  The contents of the receiver as an enumeration type, coercing to `typeEnumerated` if necessary.
- [var int32Value: Int32](nsappleeventdescriptor/int32value.md)
  The contents of the receiver as an integer, coercing (to `typeSInt32`) if necessary.
- [var numberOfItems: Int](nsappleeventdescriptor/numberofitems.md)
  The number of descriptors in the receiver’s descriptor list.
- [var stringValue: String?](nsappleeventdescriptor/stringvalue.md)
  The contents of the receiver as a Unicode text string, coercing to `typeUnicodeText` if necessary.
- [var typeCodeValue: OSType](nsappleeventdescriptor/typecodevalue.md)
  The contents of the receiver as a type, coercing to `typeType` if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/data)*