# OpenDirectory Functions

**Framework**: Open Directory  
**Role**: API Collection

This document describes the functions, constants, and data types used to interact with Open Directory.

## Topics

### Working with the Open Directory Context
- [func ODContextGetTypeID() -> CFTypeID](./odcontextgettypeid%28%29.md)
  Returns the type ID for the Open Directory context.
### Working with Nodes
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopydetails%28_,_,_%29.md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopyRecord(ODNodeRef!, String!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](./odnodecopyrecord%28_,_,_,_,_%29.md)
  Returns a reference to a record of a node.
- [func ODNodeCopySubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysubnodenames%28_,_%29.md)
  Returns the names of subnodes for a given node.
- [func ODNodeCopySupportedAttributes(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysupportedattributes%28_,_,_%29.md)
  Returns an array of attribute types supported by a given node.
- [func ODNodeCopySupportedRecordTypes(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysupportedrecordtypes%28_,_%29.md)
  Returns an array of the record types supported by a given node.
- [func ODNodeCopyUnreachableSubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopyunreachablesubnodenames%28_,_%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.
- [func ODNodeCreateCopy(CFAllocator!, ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatecopy%28_,_,_%29.md)
  Returns a copy of an existing node.
- [func ODNodeCreateRecord(ODNodeRef!, String!, CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](./odnodecreaterecord%28_,_,_,_,_%29.md)
  Creates a record in a specified node with specified properties.
- [func ODNodeCreateWithName(CFAllocator!, ODSessionRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatewithname%28_,_,_,_%29.md)
  Returns a new node created with a specified name.
- [func ODNodeCreateWithNodeType(CFAllocator!, ODSessionRef!, ODNodeType, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatewithnodetype%28_,_,_,_%29.md)
  Returns a new node created with a specified type.
- [func ODNodeCustomCall(ODNodeRef!, CFIndex, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData!](./odnodecustomcall%28_,_,_,_%29.md)
  Returns the result of a custom call to a node.
- [func ODNodeGetName(ODNodeRef!) -> Unmanaged<CFString>!](./odnodegetname%28_%29.md)
  Returns the name of a node.
- [func ODNodeGetTypeID() -> CFTypeID](./odnodegettypeid%28%29.md)
  Returns the type ID for an Open Directory node.
- [func ODNodeSetCredentials(ODNodeRef!, String!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetcredentials%28_,_,_,_,_%29.md)
  Sets credentials for interacting with a node.
- [func ODNodeSetCredentialsExtended(ODNodeRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetcredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets credentials for interacting with a node using a specified authentication method.
### Working with Queries
- [func ODQueryCopyResults(ODQueryRef!, Bool, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odquerycopyresults%28_,_,_%29.md)
  Returns results from a query synchronously.
- [func ODQueryCreateWithNode(CFAllocator!, ODNodeRef!, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnode%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query with a node using provided parameters.
- [func ODQueryCreateWithNodeType(CFAllocator!, ODNodeType, CFTypeRef!, String!, ODMatchType, CFTypeRef!, CFTypeRef!, CFIndex, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODQueryRef>!](./odquerycreatewithnodetype%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a query for a particular node type using provided parameters.
- [func ODQueryGetTypeID() -> CFTypeID](./odquerygettypeid%28%29.md)
  Returns the type ID for an Open Directory query.
- [func ODQueryScheduleWithRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryschedulewithrunloop%28_,_,_%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func ODQuerySetCallback(ODQueryRef!, ODQueryCallback!, UnsafeMutableRawPointer!)](./odquerysetcallback%28_,_,_%29.md)
  Sets the callback for an asynchronous query.
- [func ODQuerySetDispatchQueue(ODQueryRef!, dispatch_queue_t!)](./odquerysetdispatchqueue%28_,_%29.md)
  Retrieves results from a query asynchronously by adding the query to a dispatch queue.
- [func ODQuerySynchronize(ODQueryRef!)](./odquerysynchronize%28_%29.md)
  Restarts a query, disposing of any results it has obtained.
- [func ODQueryUnscheduleFromRunLoop(ODQueryRef!, CFRunLoop!, CFString!)](./odqueryunschedulefromrunloop%28_,_,_%29.md)
  Removes a query from a specified run loop.
### Working with Records
- [func ODRecordAddMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddmember%28_,_,_%29.md)
  Adds a record as a member of a group record.
- [func ODRecordAddValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddvalue%28_,_,_,_%29.md)
  Adds a value to an attribute of a record.
- [func ODRecordChangePassword(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordchangepassword%28_,_,_,_%29.md)
  Changes the password of a record.
- [func ODRecordContainsMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordcontainsmember%28_,_,_%29.md)
  Returns whether a group record contains a given record.
- [func ODRecordCopyDetails(ODRecordRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopydetails%28_,_,_%29.md)
  Returns the values of a record’s attributes.
- [func ODRecordCopyValues(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odrecordcopyvalues%28_,_,_%29.md)
  Returns the value of a single attribute of a record.
- [func ODRecordDelete(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecorddelete%28_,_%29.md)
  Deletes a record from a node and invalidates the record.
- [func ODRecordGetRecordName(ODRecordRef!) -> Unmanaged<CFString>!](./odrecordgetrecordname%28_%29.md)
  Returns the official name of a record.
- [func ODRecordGetRecordType(ODRecordRef!) -> Unmanaged<CFString>!](./odrecordgetrecordtype%28_%29.md)
  Returns the type of a record.
- [func ODRecordGetTypeID() -> CFTypeID](./odrecordgettypeid%28%29.md)
  Returns the type ID for a record.
- [func ODRecordRemoveMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremovemember%28_,_,_%29.md)
  Removes a record as a member from a specified group record.
- [func ODRecordRemoveValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremovevalue%28_,_,_,_%29.md)
  Removes a value from a record’s attribute.
- [func ODRecordSetNodeCredentials(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentials%28_,_,_,_%29.md)
  Sets node authentication credentials for a given record.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetvalue%28_,_,_,_%29.md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsynchronize%28_,_%29.md)
  Synchronizes a record with the directory to get current data and commit changes.
- [func ODRecordVerifyPassword(ODRecordRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordverifypassword%28_,_,_%29.md)
  Verifies a given password for a record.
- [func ODRecordVerifyPasswordExtended(ODRecordRef!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordverifypasswordextended%28_,_,_,_,_,_%29.md)
  Verifies a given password for a record given a specified authentication method.
### Working with Sessions
- [func ODSessionCopyNodeNames(CFAllocator!, ODSessionRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odsessioncopynodenames%28_,_,_%29.md)
  Returns the names of nodes registered in a given session.
- [func ODSessionCreate(CFAllocator!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODSessionRef>!](./odsessioncreate%28_,_,_%29.md)
  Creates a session to be passed to node functions.
- [func ODSessionGetTypeID() -> CFTypeID](./odsessiongettypeid%28%29.md)
  Returns the type ID for a session.
### Data Types
- [typealias ODAttributeType](./odattributetype.md)
  An Open Directory attribute type.
- [typealias ODAuthenticationType](./odauthenticationtype.md)
  An Open Directory authentication type.
- [class ODContext](./odcontext.md)
  An Open Directory context type.
- [class ODNodeRef](./odnoderef.md)
  An Open Directory node type.
- [class ODQueryRef](./odqueryref.md)
  An Open Directory query type.
- [class ODRecordRef](./odrecordref.md)
  An Open Directory record type.
- [class ODSessionRef](./odsessionref.md)
  An Open Directory session type.
- [typealias ODMatchType](./odmatchtype.md)
  An Open Directory match type.
- [typealias ODNodeType](./odnodetype.md)
  An Open Directory node type.
- [typealias ODQueryCallback](./odquerycallback.md)
  A callback function called as results from a scheduled query are returned.
- [typealias ODRecordType](./odrecordtype.md)
  An Open Directory record type.
### Constants
- [Session Keys](./session-keys.md)
  Keys used when specifying session information.
- [Node Types](./api-1497602-node-types.md)
  Open Directory node types.
- [Match Types](./match-types.md)
  Types of matches used for searches.
- [Record Types](./record-types.md)
  Types of Open Directory records.
- [General Attribute Types](./general-attribute-types.md)
  Types of Open Directory attributes.
- [Configuration Attribute Types](./configuration-attribute-types.md)
  Types of Open Directory attributes specifically for use with configure nodes.
- [Authentication Types](./authentication-types.md)
  Types of authentication available in Open Directory.
### Functions
- [func ODNodeAddAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodeaddaccountpolicy%28_,_,_,_%29.md)
- [func ODNodeCopyAccountPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](./odnodecopyaccountpolicies%28_,_%29.md)
- [func ODNodeCopyPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopypolicies%28_,_%29.md)
- [func ODNodeCopySupportedPolicies(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopysupportedpolicies%28_,_%29.md)
- [func ODNodeCustomFunction(ODNodeRef!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFTypeRef!](./odnodecustomfunction%28_,_,_,_%29.md)
- [func ODNodePasswordContentCheck(ODNodeRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodepasswordcontentcheck%28_,_,_,_%29.md)
- [func ODNodeRemoveAccountPolicy(ODNodeRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnoderemoveaccountpolicy%28_,_,_,_%29.md)
- [func ODNodeRemovePolicy(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnoderemovepolicy%28_,_,_%29.md)
- [func ODNodeSetAccountPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetaccountpolicies%28_,_,_%29.md)
- [func ODNodeSetPolicies(ODNodeRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetpolicies%28_,_,_%29.md)
- [func ODNodeSetPolicy(ODNodeRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetpolicy%28_,_,_,_%29.md)
- [func ODRecordAddAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddaccountpolicy%28_,_,_,_%29.md)
- [func ODRecordAuthenticationAllowed(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordauthenticationallowed%28_,_%29.md)
- [func ODRecordCopyAccountPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFDictionary!](./odrecordcopyaccountpolicies%28_,_%29.md)
- [func ODRecordCopyEffectivePolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopyeffectivepolicies%28_,_%29.md)
- [func ODRecordCopyPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopypolicies%28_,_%29.md)
- [func ODRecordCopySupportedPolicies(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopysupportedpolicies%28_,_%29.md)
- [func ODRecordPasswordChangeAllowed(ODRecordRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordpasswordchangeallowed%28_,_,_%29.md)
- [func ODRecordRemoveAccountPolicy(ODRecordRef!, CFDictionary!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremoveaccountpolicy%28_,_,_,_%29.md)
- [func ODRecordRemovePolicy(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremovepolicy%28_,_,_%29.md)
- [func ODRecordSecondsUntilAuthenticationsExpire(ODRecordRef!) -> Int64](./odrecordsecondsuntilauthenticationsexpire%28_%29.md)
- [func ODRecordSecondsUntilPasswordExpires(ODRecordRef!) -> Int64](./odrecordsecondsuntilpasswordexpires%28_%29.md)
- [func ODRecordSetAccountPolicies(ODRecordRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetaccountpolicies%28_,_,_%29.md)
- [func ODRecordSetPolicies(ODRecordRef!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetpolicies%28_,_,_%29.md)
- [func ODRecordSetPolicy(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetpolicy%28_,_,_,_%29.md)
- [func ODRecordWillAuthenticationsExpire(ODRecordRef!, UInt64) -> Bool](./odrecordwillauthenticationsexpire%28_,_%29.md)
- [func ODRecordWillPasswordExpire(ODRecordRef!, UInt64) -> Bool](./odrecordwillpasswordexpire%28_,_%29.md)

## See Also

### Reference
- [OpenDirectory Enumerations](./opendirectory-enumerations.md)
- [OpenDirectory Constants](./opendirectory-constants.md)
- [OpenDirectory Data Types](./opendirectory-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/opendirectory-functions)*