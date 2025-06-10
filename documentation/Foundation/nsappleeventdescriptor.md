# NSAppleEventDescriptor

**Framework**: Foundation  
**Kind**: class

A wrapper for the Apple event descriptor data type.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSAppleEventDescriptor
```

#### Overview

An instance of [`NSAppleEventDescriptor`](nsappleeventdescriptor.md) represents a descriptor—the basic building block for Apple events. This class is a wrapper for the underlying Apple event descriptor data type, [`AEDesc`](https://developer.apple.com/documentation/coreservices/aedesc). Scriptable Cocoa applications frequently work with instances of [`NSAppleEventDescriptor`](nsappleeventdescriptor.md), but should rarely need to work directly with the [`AEDesc`](https://developer.apple.com/documentation/coreservices/aedesc) data structure.

A  is a data structure that stores data and an accompanying four-character code. A descriptor can store a value, or it can store a list of other descriptors (which may also be lists). All the information in an Apple event is stored in descriptors and lists of descriptors, and every Apple event is itself a descriptor list that matches certain criteria.

> ❗ **Important**:  An instance of `NSAppleEventDescriptor` can represent any kind of descriptor, from a simple value descriptor, to a descriptor list, to a full-fledged Apple event.

Descriptors can be used to build arbitrarily complex containers, so that one Apple event can represent a script statement such as `tell application "TextEdit" to get word 3 of paragraph 6 of document 3`.

In working with Apple event descriptors, it can be useful to understand some of the underlying data types. You’ll find terms such as descriptor, descriptor list, Apple event record, and Apple event defined in Building an Apple Event in Apple Events Programming Guide. You’ll also find information on the four-character codes used to identify information within a descriptor. Apple event data types are defined in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager). The values of many four-character codes used by Apple (and in some cases reused by developers) can be found in [`AppleScript Terminology and Apple Event Codes`](https://developer.apple.comhttp://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html).

The most common reason to construct an Apple event with an instance of `NSAppleEventDescriptor` is to supply information in a return Apple event. The most common situation where you might need to extract information from an Apple event (as an instance of `NSAppleEventDescriptor`) is when an Apple event handler installed by your application is invoked, as described in “Installing an Apple Event Handler” in [`How Cocoa Applications Handle Apple Events`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239). In addition, if you execute an AppleScript script using the `NSAppleScript` class, you get an instance of `NSAppleEventDescriptor` as the return value, from which you can extract any required information.

When you work with an instance of `NSAppleEventDescriptor`, you can access the underlying descriptor directly, if necessary, with the [`aeDesc`](nsappleeventdescriptor/aedesc.md) method. Other methods, including [`descriptorWithDescriptorType:bytes:length:`](nsappleeventdescriptor/descriptorwithdescriptortype:bytes:length:.md) make it possible to create and initialize instances of `NSAppleEventDescriptor` without creating temporary instances of `NSData`.

The designated initializer for `NSAppleEventDescriptor` is [`init(aeDescNoCopy:)`](nsappleeventdescriptor/init(aedescnocopy:).md). However, it is unlikely that you will need to create a subclass of `NSAppleEventDescriptor`.

Cocoa doesn’t currently provide a mechanism for applications to directly send raw Apple events (though compiling and executing an AppleScript script with `NSAppleScript` may result in Apple events being sent). However, Cocoa applications have full access to the Apple Event Manager C APIs for working with Apple events. So, for example, you might use an instance of  `NSAppleEventDescriptor` to assemble an Apple event and call the Apple Event Manager function `AESend(_:_:_:_:_:_:_:)` to send it.

If you need to send Apple events, or if you need more information on some of the Apple event concepts described here, see Apple Events Programming Guide and [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

## Topics

### Creating and Initializing Descriptors
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
### Getting Information About a Descriptor
- [var aeDesc: UnsafePointer<AEDesc>?](nsappleeventdescriptor/aedesc.md)
  The `AEDesc` structure encapsulated by the receiver, if it has one.
- [var booleanValue: Bool](nsappleeventdescriptor/booleanvalue.md)
  The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.
- [func coerce(toDescriptorType: DescType) -> NSAppleEventDescriptor?](nsappleeventdescriptor/coerce(todescriptortype:).md)
  Returns a descriptor obtained by coercing the receiver to the specified type.
- [var data: Data](nsappleeventdescriptor/data.md)
  The receiver’s data.
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
### Working With List Descriptors
- [func atIndex(Int) -> NSAppleEventDescriptor?](nsappleeventdescriptor/atindex(_:).md)
  Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [func insert(NSAppleEventDescriptor, at: Int)](nsappleeventdescriptor/insert(_:at:).md)
  Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.
- [func remove(at: Int)](nsappleeventdescriptor/remove(at:).md)
  Removes the descriptor at the specified (one-based) position in the receiving descriptor list.
### Working With Record Descriptors
- [func forKeyword(AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/forkeyword(_:).md)
  Returns the receiver’s descriptor for the specified keyword.
- [func keywordForDescriptor(at: Int) -> AEKeyword](nsappleeventdescriptor/keywordfordescriptor(at:).md)
  Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [func remove(withKeyword: AEKeyword)](nsappleeventdescriptor/remove(withkeyword:).md)
  Removes the receiver’s descriptor identified by the specified keyword.
- [func setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setdescriptor(_:forkeyword:).md)
  Adds a descriptor, identified by a keyword, to the receiver.
### Working With Apple Event Descriptors
- [func attributeDescriptor(forKeyword: AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/attributedescriptor(forkeyword:).md)
  Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [var eventClass: AEEventClass](nsappleeventdescriptor/eventclass.md)
  The event class for the receiver.
- [var eventID: AEEventID](nsappleeventdescriptor/eventid.md)
  The event ID for the receiver.
- [func paramDescriptor(forKeyword: AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/paramdescriptor(forkeyword:).md)
  Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [func removeParamDescriptor(withKeyword: AEKeyword)](nsappleeventdescriptor/removeparamdescriptor(withkeyword:).md)
  Removes the receiver’s parameter descriptor identified by the specified keyword.
- [var returnID: AEReturnID](nsappleeventdescriptor/returnid.md)
  The receiver’s return ID (the ID for a reply Apple event).
- [func setAttribute(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setattribute(_:forkeyword:).md)
  Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [func setParam(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setparam(_:forkeyword:).md)
  Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [var transactionID: AETransactionID](nsappleeventdescriptor/transactionid.md)
  The receiver’s transaction ID, if any.
### Supporting Types
- [NSAppleEventDescriptor.SendOptions](nsappleeventdescriptor/sendoptions.md)
### Initializers
- [init(applicationURL: URL)](nsappleeventdescriptor/init(applicationurl:).md)
- [init(bundleIdentifier: String)](nsappleeventdescriptor/init(bundleidentifier:).md)
- [init(date: Date)](nsappleeventdescriptor/init(date:).md)
- [init(double: Double)](nsappleeventdescriptor/init(double:).md)
- [init(fileURL: URL)](nsappleeventdescriptor/init(fileurl:).md)
- [init(processIdentifier: pid_t)](nsappleeventdescriptor/init(processidentifier:).md)
### Instance Properties
- [var dateValue: Date?](nsappleeventdescriptor/datevalue.md)
- [var doubleValue: Double](nsappleeventdescriptor/doublevalue.md)
- [var fileURLValue: URL?](nsappleeventdescriptor/fileurlvalue.md)
- [var isRecordDescriptor: Bool](nsappleeventdescriptor/isrecorddescriptor.md)
### Instance Methods
- [func sendEvent(options: NSAppleEventDescriptor.SendOptions, timeout: TimeInterval) throws -> NSAppleEventDescriptor](nsappleeventdescriptor/sendevent(options:timeout:).md)
### Type Methods
- [class func currentProcess() -> NSAppleEventDescriptor](nsappleeventdescriptor/currentprocess.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class NSAppleEventManager](nsappleeventmanager.md)
  A mechanism for registering handler routines for specific types of Apple events and dispatching events to those handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor)*