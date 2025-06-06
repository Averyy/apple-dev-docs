# appleEvent(withEventClass:eventID:targetDescriptor:returnID:transactionID:)

**Framework**: Foundation  
**Kind**: method

Creates a descriptor that represents an Apple event, initialized according to the specified information.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func appleEvent(withEventClass eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor
```

#### Return Value

A descriptor for an Apple event, initialized according to the specified parameter values, or `nil` if an error occurs.

#### Discussion

Constants such as `kAutoGenerateReturnID` and `kAnyTransactionID` are defined in `AE.framework`, a subframework of `ApplicationServices.framework`.

## Parameters

- `eventClass`: The event class to be set in the returned descriptor.
- `eventID`: The event ID to be set in the returned descriptor.
- `targetDescriptor`: A pointer to a descriptor that identifies the target application for the Apple event. Passing   results in an Apple event descriptor that has no   attribute (it is valid for an Apple event to have no target address attribute).
- `returnID`: The return ID to be set in the returned descriptor. If you pass a value of  , the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID.
- `transactionID`: The transaction ID to be set in the returned descriptor. A transaction is a sequence of Apple events that are sent back and forth between client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify   if the Apple event is not one of a series of interdependent Apple events.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
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
- [convenience init(recordDescriptor: ())](nsappleeventdescriptor/init(recorddescriptor:).md)
  Initializes a newly allocated instance as a descriptor that is an Apple event record.
- [init(aeDescNoCopy: UnsafePointer<AEDesc>)](nsappleeventdescriptor/init(aedescnocopy:).md)
  Initializes a newly allocated instance as a descriptor for the specified Carbon `AEDesc` structure.
- [convenience init?(descriptorType: DescType, bytes: UnsafeRawPointer?, length: Int)](nsappleeventdescriptor/init(descriptortype:bytes:length:).md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [convenience init?(descriptorType: DescType, data: Data?)](nsappleeventdescriptor/init(descriptortype:data:).md)
  Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [convenience init(eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID)](nsappleeventdescriptor/init(eventclass:eventid:targetdescriptor:returnid:transactionid:).md)
  Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/appleevent(witheventclass:eventid:targetdescriptor:returnid:transactionid:))*