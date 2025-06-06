# Collaboration

**Framework**: Collaboration  
**Kind**: module

Find and access identities, that is, users and groups. Display the Identity Picker, which lets users create and select identities.

**Availability**:
- macOS 10.5+

#### Overview

The Collaboration framework allows developers to monitor identities and their attributes. Identities reside in an identity authority, which can be either local to a user’s system, or on a network directory. The Collaboration framework also manages a sheet, known as the identity picker, to allow applications to select identities.

The Collaboration framework works closely with the Core Services Identity APIs to form the Identity Services technology. If you need the ability to create and manipulate identities read [`Core Services Identity Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/index.html#//apple_ref/doc/uid/TP40004673).

## Topics

### Classes
- [class CBGroupIdentity](cbgroupidentity.md)
  An object of the `CBGroupIdentity` class represents a group identity and is used for viewing the attributes of group identities from an identity authority. The principal attributes of a `CBGroupIdentity` object are a POSIX group identifier (GID) and a list of members.
- [class CBIdentity](cbidentity.md)
  A `CBIdentity` object is used for accessing the attributes of an identity stored in an identity authority. You can use an identity object for finding identities, and storing them in an access control list (ACL). If you need to edit these attributes, take advantage of the `CSIdentity` class in Core Services.
- [class CBIdentityAuthority](cbidentityauthority.md)
  An identity authority is a database that stores information about identities. The `CBIdentityAuthority` class defines one or more identity authorities. You can search this database for identities in conjunction with the `CBIdentity` class factory methods.
- [class CBIdentityPicker](cbidentitypicker.md)
  A `CBIdentityPicker` object allows a user to select identities—for example, user or group objects—that it wants one or more services or shared resources to have access to. An identity picker can be displayed either as an application-modal dialog or as a sheet attached to a document window. An identity picker returns the selected records to be added to access control lists using Collaboration. If a selected record is not a user or group identity, then an identity picker prompts the user for additional information—such as a password—to promote that record to a sharing account.
- [class CBUserIdentity](cbuseridentity.md)
  An object of the `CBUserIdentity` class represents a user identity and is used for accessing the attributes of a user identity from an identity authority. The principal attributes of `CBUserIdentity` are a POSIX user identifier (UID), password, and certificate.

## See Also

- [Core Services Identity Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/index.html#//apple_ref/doc/uid/TP40004673)
- [Identity Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Collaboration)*