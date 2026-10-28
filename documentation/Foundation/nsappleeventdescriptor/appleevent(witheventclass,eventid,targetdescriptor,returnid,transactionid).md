# appleEvent(withEventClass:eventID:targetDescriptor:returnID:transactionID:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a descriptor that represents an Apple event, initialized according to the specified information.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func appleEvent(withEventClass eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor
```

```objc
+ (NSAppleEventDescriptor *) appleEventWithEventClass:(AEEventClass) eventClass eventID:(AEEventID) eventID targetDescriptor:(NSAppleEventDescriptor *) targetDescriptor returnID:(AEReturnID) returnID transactionID:(AETransactionID) transactionID;
```

## Return Value

A descriptor for an Apple event, initialized according to the specified parameter values, or `nil` if an error occurs.

## Discussion

Constants such as `kAutoGenerateReturnID` and `kAnyTransactionID` are defined in `AE.framework`, a subframework of `ApplicationServices.framework`.

## Parameters

- `eventClass`: The event class to be set in the returned descriptor.
- `eventID`: The event ID to be set in the returned descriptor.
- `targetDescriptor`: A pointer to a descriptor that identifies the target application for the Apple event. Passing `nil` results in an Apple event descriptor that has no `keyAddressAttr` attribute (it is valid for an Apple event to have no target address attribute).
- `returnID`: The return ID to be set in the returned descriptor. If you pass a value of `kAutoGenerateReturnID`, the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID.
- `transactionID`: The transaction ID to be set in the returned descriptor. A transaction is a sequence of Apple events that are sent back and forth between client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify `kAnyTransactionID` if the Apple event is not one of a series of interdependent Apple events.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Creating and Initializing Descriptors
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
- [convenience init(recordDescriptor: ())](./init%28recorddescriptor%29.md)
  Initializes a newly allocated instance as a descriptor that is an Apple event record.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/appleevent(witheventclass:eventid:targetdescriptor:returnid:transactionid:))*