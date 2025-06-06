# init(recordDescriptor:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated instance as a descriptor that is an Apple event record.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(recordDescriptor: ())
```

#### Return Value

The initialized Apple event record, or `nil` if an error occurs.

#### Discussion

An Apple event record is a descriptor whose data is a set of descriptors keyed by four-character codes. You can add information to the descriptor with methods such as [`setAttribute(_:forKeyword:)`](nsappleeventdescriptor/setattribute(_:forkeyword:).md), [`setDescriptor(_:forKeyword:)`](nsappleeventdescriptor/setdescriptor(_:forkeyword:).md), and [`setParam(_:forKeyword:)`](nsappleeventdescriptor/setparam(_:forkeyword:).md).

## See Also

- [class func appleEvent(withEventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor](nsappleeventdescriptor/appleevent(witheventclass:eventid:targetdescriptor:returnid:transactionid:).md)
  Creates a descriptor that represents an Apple event, initialized according to the specified information.
- [init(boolean: Bool)](nsappleeventdescriptor/init(boolean:).md)
  Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.
- [init(enumCode: OSType)](nsappleeventdescriptor/init(enumcode:).md)
  Creates a descriptor initialized with type `typeEnumerated` that stores the specified enumerator data type value.
- [init(int32: Int32)](nsappleeventdescriptor/init(int32:).md)
  Creates a descriptor initialized with Apple event type `typeSInt32` that stores the specified integer value.
- [init(string: String)](nsappleeventdescriptor/init(string:).md)
  Creates a descriptor initialized with type `typeUnicodeText` that stores the text from the specified string.
- [init(typeCode: OSType)](nsappleeventdescriptor/init(typecode:).md)
  Creates a descriptor initialized with type `typeType` that stores the specified type value.
- [class func list() -> NSAppleEventDescriptor](nsappleeventdescriptor/list.md)
  Creates and initializes an empty list descriptor.
- [class func null() -> NSAppleEventDescriptor](nsappleeventdescriptor/null.md)
  Creates and initializes a descriptor with no parameter or attribute values set.
- [class func record() -> NSAppleEventDescriptor](nsappleeventdescriptor/record.md)
  Creates and initializes a descriptor for an Apple event record whose data has yet to be set.
- [convenience init(listDescriptor: ())](nsappleeventdescriptor/init(listdescriptor:).md)
  Initializes a newly allocated instance as an empty list descriptor.
- [init(aeDescNoCopy: UnsafePointer<AEDesc>)](nsappleeventdescriptor/init(aedescnocopy:).md)
  Initializes a newly allocated instance as a descriptor for the specified Carbon `AEDesc` structure.
- [convenience init?(descriptorType: DescType, bytes: UnsafeRawPointer?, length: Int)](nsappleeventdescriptor/init(descriptortype:bytes:length:).md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [convenience init?(descriptorType: DescType, data: Data?)](nsappleeventdescriptor/init(descriptortype:data:).md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [convenience init(eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID)](nsappleeventdescriptor/init(eventclass:eventid:targetdescriptor:returnid:transactionid:).md)
  Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(recorddescriptor:))*