# CNContactRelation

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

An immutable object that represents the relationship between one contact to another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactRelation
```

```objc
@interface CNContactRelation : NSObject
```

#### Overview

`CNContactRelation` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating a Contact Relation Object
- [init(name: String)](./cncontactrelation/init%28name%29.md)
  Creates an object with the name of the related contact.
- [+ contactRelationWithName:](./cncontactrelation/contactrelationwithname_.md)
  Instantiate a class instance with the name of the related contact.
### Getting the Relation Name
- [var name: String](./cncontactrelation/name.md)
  The name of the related contact.
### Getting the Common Relationship Labels
- [let CNLabelContactRelationSpouse: String](./cnlabelcontactrelationspouse.md)
  The label for the contact’s spouse.
- [let CNLabelContactRelationPartner: String](./cnlabelcontactrelationpartner.md)
  The label for the contact’s partner.
- [let CNLabelContactRelationDaughter: String](./cnlabelcontactrelationdaughter.md)
  The label for the contact’s daughter.
- [let CNLabelContactRelationSon: String](./cnlabelcontactrelationson.md)
  The label for the contact’s son.
- [let CNLabelContactRelationChild: String](./cnlabelcontactrelationchild.md)
  The label for the contact’s child.
- [let CNLabelContactRelationFather: String](./cnlabelcontactrelationfather.md)
  The label for the contact’s father.
- [let CNLabelContactRelationMother: String](./cnlabelcontactrelationmother.md)
  The label for the contact’s mother.
- [let CNLabelContactRelationParent: String](./cnlabelcontactrelationparent.md)
  The label for the contact’s parent.
- [let CNLabelContactRelationBrother: String](./cnlabelcontactrelationbrother.md)
  The label for the contact’s brother.
- [let CNLabelContactRelationSister: String](./cnlabelcontactrelationsister.md)
  The label for the contact’s sister.
- [let CNLabelContactRelationFriend: String](./cnlabelcontactrelationfriend.md)
  The label for the contact’s friend.
- [let CNLabelContactRelationAssistant: String](./cnlabelcontactrelationassistant.md)
  The label for the contact’s assistant.
- [let CNLabelContactRelationManager: String](./cnlabelcontactrelationmanager.md)
  The label for the contact’s manager.
### Initializers
- [init?(coder: NSCoder)](./cncontactrelation/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactrelation)*