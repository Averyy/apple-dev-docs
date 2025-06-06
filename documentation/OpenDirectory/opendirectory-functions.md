# OpenDirectory Functions

**Framework**: Open Directory

This document describes the functions, constants, and data types used to interact with Open Directory.

## Topics

### Working with the Open Directory Context
- [func ODContextGetTypeID() -> CFTypeID](odcontextgettypeid().md)
  Returns the type ID for the Open Directory context.
### Working with Nodes
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopydetails(_:_:_:).md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopyRecord(ODNodeRef!, String!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](odnodecopyrecord(_:_:_:_:_:).md)
  Returns a reference to a record of a node.
- [func ODNodeCopySubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysubnodenames(_:_:).md)
  Returns the names of subnodes for a given node.
- [func ODNodeCopySupportedAttributes(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysupportedattributes(_:_:_:).md)
  Returns an array of attribute types supported by a given node.
- [func ODNodeCopySupportedRecordTypes(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysupportedrecordtypes(_:_:).md)
  Returns an array of the record types supported by a given node.
- [func ODNodeCopyUnreachableSubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopyunreachablesubnodenames(_:_:).md)
  Returns an array of the subnodes of a given node that are currently unreachable.
- [func ODNodeCreateCopy(CFAllocator!, ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatecopy(_:_:_:).md)
  Returns a copy of an existing node.
- [func ODNodeCreateRecord(ODNodeRef!, String!, CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](odnodecreaterecord(_:_:_:_:_:).md)
  Creates a record in a specified node with specified properties.
- [func ODNodeCreateWithName(CFAllocator!, ODSessionRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatewithname(_:_:_:_:).md)
  Returns a new node created with a specified name.
- [func ODNodeCreateWithNodeType(CFAllocator!, ODSessionRef!, ODNodeType, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatewithnodetype(_:_:_:_:).md)
  Returns a new node created with a specified type.
- [func ODNodeCustomCall(ODNodeRef!, CFIndex, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData!](odnodecustomcall(_:_:_:_:).md)
  Returns the result of a custom call to a node.
- [func ODNodeGetName(ODNodeRef!) -> Unmanaged<CFString>!](odnodegetname(_:).md)
  Returns the name of a node.
- [func ODNodeGetTypeID() -> CFTypeID](odnodegettypeid().md)
  Returns the type ID for an Open Directory node.
- [func ODNodeSetCredentials(ODNodeRef!, String!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetcredentials(_:_:_:_:_:).md)
  Sets credentials for interacting with a node.
- [func ODNodeSetCredentialsExtended(ODNodeRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetcredentialsextended(_:_:_:_:_:_:_:).md)
  Sets credentials for interacting with a node using a specified authentication method.
### Working with Queries
- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odquerycopyresults(_:_:_:).md)
  Returns results from a query synchronously.
- [func ODQueryCreateWithNode(CFAllocator!, ODNodeRef!, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](odquerycreatewithnode(_:_:_:_:_:_:_:_:_:).md)
  Creates a query with a node using provided parameters.
- [func ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](odquerycreatewithnodetype(_:_:_:_:_:_:_:_:_:).md)
  Creates a query for a particular node type using provided parameters.
- [func ODQueryGetTypeID() -> CFTypeID](odquerygettypeid().md)
  Returns the type ID for an Open Directory query.
- [func ODQueryScheduleWithRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryschedulewithrunloop(_:_:_:).md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](odquerysetcallback(_:_:_:).md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](odquerysetdispatchqueue(_:_:).md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](odquerysynchronize(_:).md)
  Restarts a query, disposing of any results it has obtained.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](odqueryunschedulefromrunloop(_:_:_:).md)
  Removes a query from a specified run loop.
### Working with Records
- [func ODRecordAddMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddmember(_:_:_:).md)
  Adds a record as a member of a group record.
- [func ODRecordAddValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddvalue(_:_:_:_:).md)
  Adds a value to an attribute of a record.
- [func ODRecordChangePassword(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordchangepassword(_:_:_:_:).md)
  Changes the password of a record.
- [func ODRecordContainsMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordcontainsmember(_:_:_:).md)
  Returns whether a group record contains a given record.
- [func ODRecordCopyDetails(ODRecordRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopydetails(_:_:_:).md)
  Returns the values of a record’s attributes.
- [func ODRecordCopyValues(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odrecordcopyvalues(_:_:_:).md)
  Returns the value of a single attribute of a record.
- [func ODRecordDelete(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecorddelete(_:_:).md)
  Deletes a record from a node and invalidates the record.
- [func ODRecordGetRecordName(ODRecordRef!) -> Unmanaged<CFString>!](odrecordgetrecordname(_:).md)
  Returns the official name of a record.
- [func ODRecordGetRecordType(ODRecordRef!) -> Unmanaged<CFString>!](odrecordgetrecordtype(_:).md)
  Returns the type of a record.
- [func ODRecordGetTypeID() -> CFTypeID](odrecordgettypeid().md)
  Returns the type ID for a record.
- [func ODRecordRemoveMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremovemember(_:_:_:).md)
  Removes a record as a member from a specified group record.
- [func ODRecordRemoveValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremovevalue(_:_:_:_:).md)
  Removes a value from a record’s attribute.
- [func ODRecordSetNodeCredentials(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetnodecredentials(_:_:_:_:).md)
  Sets node authentication credentials for a given record.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetnodecredentialsextended(_:_:_:_:_:_:_:).md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetvalue(_:_:_:_:).md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsynchronize(_:_:).md)
  Synchronizes a record with the directory to get current data and commit changes.
- [func ODRecordVerifyPassword(ODRecordRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordverifypassword(_:_:_:).md)
  Verifies a given password for a record.
- [func ODRecordVerifyPasswordExtended(ODRecordRef!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordverifypasswordextended(_:_:_:_:_:_:).md)
  Verifies a given password for a record given a specified authentication method.
### Working with Sessions
- [func ODSessionCopyNodeNames(CFAllocator!, ODSessionRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odsessioncopynodenames(_:_:_:).md)
  Returns the names of nodes registered in a given session.
- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](odsessioncreate(_:_:_:).md)
  Creates a session to be passed to node functions.
- [func ODSessionGetTypeID() -> CFTypeID](odsessiongettypeid().md)
  Returns the type ID for a session.
### Data Types
- [typealias ODAttributeType](odattributetype.md)
  An Open Directory attribute type.
- [typealias ODAuthenticationType](odauthenticationtype.md)
  An Open Directory authentication type.
- [class ODContext](odcontext.md)
  An Open Directory context type.
- [class ODNodeRef](odnoderef.md)
  An Open Directory node type.
- [class ODQueryRef](odqueryref.md)
  An Open Directory query type.
- [class ODRecordRef](odrecordref.md)
  An Open Directory record type.
- [class ODSessionRef](odsessionref.md)
  An Open Directory session type.
- [typealias ODMatchType](odmatchtype.md)
  An Open Directory match type.
- [typealias ODNodeType](odnodetype.md)
  An Open Directory node type.
- [typealias ODQueryCallback](odquerycallback.md)
  A callback function called as results from a scheduled query are returned.
- [typealias ODRecordType](odrecordtype.md)
  An Open Directory record type.
- [_ODAttributeType](odattributetype.md)
  An Open Directory attribute type.
- [_ODAuthenticationType](odauthenticationtype.md)
  An Open Directory authentication type.
- [_ODRecordType](odrecordtype.md)
  An Open Directory record type.
### Constants
- [Session Keys](session-keys.md)
  Keys used when specifying session information.
- [Node Types](1497602-node-types.md)
  Open Directory node types.
- [Match Types](match-types.md)
  Types of matches used for searches.
- [Record Types](record-types.md)
  Types of Open Directory records.
- [General Attribute Types](general-attribute-types.md)
  Types of Open Directory attributes.
- [Configuration Attribute Types](configuration-attribute-types.md)
  Types of Open Directory attributes specifically for use with configure nodes.
- [Authentication Types](authentication-types.md)
  Types of authentication available in Open Directory.
### Functions
- [func ODNodeAddAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodeaddaccountpolicy(_:_:_:_:).md)
- [func ODNodeCopyAccountPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](odnodecopyaccountpolicies(_:_:).md)
- [func ODNodeCopyPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopypolicies(_:_:).md)
- [func ODNodeCopySupportedPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopysupportedpolicies(_:_:).md)
- [func ODNodeCustomFunction(ODNodeRef!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef!](odnodecustomfunction(_:_:_:_:).md)
- [func ODNodePasswordContentCheck(ODNodeRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodepasswordcontentcheck(_:_:_:_:).md)
- [func ODNodeRemoveAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnoderemoveaccountpolicy(_:_:_:_:).md)
- [func ODNodeRemovePolicy(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnoderemovepolicy(_:_:_:).md)
- [func ODNodeSetAccountPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetaccountpolicies(_:_:_:).md)
- [func ODNodeSetPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetpolicies(_:_:_:).md)
- [func ODNodeSetPolicy(ODNodeRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetpolicy(_:_:_:_:).md)
- [func ODRecordAddAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddaccountpolicy(_:_:_:_:).md)
- [func ODRecordAuthenticationAllowed(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordauthenticationallowed(_:_:).md)
- [func ODRecordCopyAccountPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](odrecordcopyaccountpolicies(_:_:).md)
- [func ODRecordCopyEffectivePolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopyeffectivepolicies(_:_:).md)
- [func ODRecordCopyPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopypolicies(_:_:).md)
- [func ODRecordCopySupportedPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopysupportedpolicies(_:_:).md)
- [func ODRecordPasswordChangeAllowed(ODRecordRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordpasswordchangeallowed(_:_:_:).md)
- [func ODRecordRemoveAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremoveaccountpolicy(_:_:_:_:).md)
- [func ODRecordRemovePolicy(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremovepolicy(_:_:_:).md)
- [func ODRecordSecondsUntilAuthenticationsExpire(ODRecordRef!) -> Int64](odrecordsecondsuntilauthenticationsexpire(_:).md)
- [func ODRecordSecondsUntilPasswordExpires(ODRecordRef!) -> Int64](odrecordsecondsuntilpasswordexpires(_:).md)
- [func ODRecordSetAccountPolicies(ODRecordRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetaccountpolicies(_:_:_:).md)
- [func ODRecordSetPolicies(ODRecordRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetpolicies(_:_:_:).md)
- [func ODRecordSetPolicy(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetpolicy(_:_:_:_:).md)
- [func ODRecordWillAuthenticationsExpire(ODRecordRef!, UInt64) -> Bool](odrecordwillauthenticationsexpire(_:_:).md)
- [func ODRecordWillPasswordExpire(ODRecordRef!, UInt64) -> Bool](odrecordwillpasswordexpire(_:_:).md)

## See Also

- [OpenDirectory Enumerations](opendirectory-enumerations.md)
- [OpenDirectory Constants](opendirectory-constants.md)
- [OpenDirectory Data Types](opendirectory-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/opendirectory-functions)*