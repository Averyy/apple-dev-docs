# CNContactRelation

**Framework**: Contacts  
**Kind**: class

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

#### Overview

`CNContactRelation` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating a Contact Relation Object
- [init(name: String)](cncontactrelation/init(name:).md)
  Creates an object with the name of the related contact.
### Getting the Relation Name
- [var name: String](cncontactrelation/name.md)
  The name of the related contact.
### Getting the Common Relationship Labels
- [let CNLabelContactRelationSpouse: String](cnlabelcontactrelationspouse.md)
  The label for the contact’s spouse.
- [let CNLabelContactRelationPartner: String](cnlabelcontactrelationpartner.md)
  The label for the contact’s partner.
- [let CNLabelContactRelationDaughter: String](cnlabelcontactrelationdaughter.md)
  The label for the contact’s daughter.
- [let CNLabelContactRelationSon: String](cnlabelcontactrelationson.md)
  The label for the contact’s son.
- [let CNLabelContactRelationChild: String](cnlabelcontactrelationchild.md)
  The label for the contact’s child.
- [let CNLabelContactRelationFather: String](cnlabelcontactrelationfather.md)
  The label for the contact’s father.
- [let CNLabelContactRelationMother: String](cnlabelcontactrelationmother.md)
  The label for the contact’s mother.
- [let CNLabelContactRelationParent: String](cnlabelcontactrelationparent.md)
  The label for the contact’s parent.
- [let CNLabelContactRelationBrother: String](cnlabelcontactrelationbrother.md)
  The label for the contact’s brother.
- [let CNLabelContactRelationSister: String](cnlabelcontactrelationsister.md)
  The label for the contact’s sister.
- [let CNLabelContactRelationFriend: String](cnlabelcontactrelationfriend.md)
  The label for the contact’s friend.
- [let CNLabelContactRelationAssistant: String](cnlabelcontactrelationassistant.md)
  The label for the contact’s assistant.
- [let CNLabelContactRelationManager: String](cnlabelcontactrelationmanager.md)
  The label for the contact’s manager.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactrelation)*