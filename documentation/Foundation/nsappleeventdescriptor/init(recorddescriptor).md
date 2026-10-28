# init(recordDescriptor:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated instance as a descriptor that is an Apple event record.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(recordDescriptor: ())
```

```objc
- (instancetype) initRecordDescriptor;
```

## Return Value

The initialized Apple event record, or `nil` if an error occurs.

## Discussion

An Apple event record is a descriptor whose data is a set of descriptors keyed by four-character codes. You can add information to the descriptor with methods such as [`setAttribute(_:forKeyword:)`](./setattribute%28_,forkeyword%29.md), [`setDescriptor(_:forKeyword:)`](./setdescriptor%28_,forkeyword%29.md), and [`setParam(_:forKeyword:)`](./setparam%28_,forkeyword%29.md).

## See Also

### Creating and Initializing Descriptors
- [class func appleEvent(withEventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor](./appleevent%28witheventclass,eventid,targetdescriptor,returnid,transactionid%29.md)
  Creates a descriptor that represents an Apple event, initialized according to the specified information.
- [init(boolean: Bool)](./init%28boolean%29.md)
  Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.
- [init(enumCode: OSType)](./init%28enumcode%29.md)
  Creates a descriptor initialized with type `typeEnumerated` that stores the specified enumerator data type value.
- [init(int32: Int32)](./init%28int32%29.md)
  Creates a descriptor initialized with Apple event type `typeSInt32` that stores the specified integer value.
- [init(string: String)](./init%28string%29.md)
  Creates a descriptor initialized with type `typeUnicodeText` that stores the text from the specified string.
- [init(typeCode: OSType)](./init%28typecode%29.md)
  Creates a descriptor initialized with type `typeType` that stores the specified type value.
- [class func list() -> NSAppleEventDescriptor](./list%28%29.md)
  Creates and initializes an empty list descriptor.
- [class func null() -> NSAppleEventDescriptor](./null%28%29.md)
  Creates and initializes a descriptor with no parameter or attribute values set.
- [class func record() -> NSAppleEventDescriptor](./record%28%29.md)
  Creates and initializes a descriptor for an Apple event record whose data has yet to be set.
- [convenience init(listDescriptor: ())](./init%28listdescriptor%29.md)
  Initializes a newly allocated instance as an empty list descriptor.
- [init(aeDescNoCopy: UnsafePointer<AEDesc>)](./init%28aedescnocopy%29-5cioa.md)
  Initializes a newly allocated instance as a descriptor for the specified Carbon `AEDesc` structure.
- [convenience init?(descriptorType: DescType, bytes: UnsafeRawPointer?, length: Int)](./init%28descriptortype,bytes,length%29.md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [convenience init?(descriptorType: DescType, data: Data?)](./init%28descriptortype,data%29.md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [convenience init(eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID)](./init%28eventclass,eventid,targetdescriptor,returnid,transactionid%29.md)
  Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.
- [+ descriptorWithDescriptorType:bytes:length:](./descriptorwithdescriptortype_bytes_length_.md)
  Creates a descriptor initialized with the specified event type that stores the specified data (from a series of bytes).
- [+ descriptorWithDescriptorType:data:](./descriptorwithdescriptortype_data_.md)
  Creates a descriptor initialized with the specified event type that stores the specified data (from an instance of `NSData`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(recorddescriptor:))*