# CNContactProperty

**Framework**: Contacts  
**Kind**: class  
**Role**: Class

An object that represents a property of a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactProperty
```

```objc
@interface CNContactProperty : NSObject
```

#### Overview

A contact (that is, an instance of [`CNContact`](./cncontact.md)) has properties, such as [`givenName`](./cncontact/givenname.md), [`phoneNumbers`](./cncontact/phonenumbers.md), and [`jobTitle`](./cncontact/jobtitle.md). Each property is represented by an instance of [`CNContactProperty`](./cncontactproperty.md), which provides a tuple that can contain three or five values, depending on whether the property is a member of an array of labeled values. For example, the [`phoneNumbers`](./cncontact/phonenumbers.md) property is a member of an array of labeled values, so the `CNContactProperty` tuple contains the contact, key, value, identifier, and label. For the [`givenName`](./cnmutablecontact/givenname.md) property, which is not contained in a labeled array, `CNContactProperty` returns a tuple that contains the contact, key, and value. The `CNContactProperty` class is used by [`CNContactPicker`](../ContactsUI/cncontactpicker.md) to return the user’s selected property.

## Topics

### Getting the Contact Object
- [var contact: CNContact](./cncontactproperty/contact.md)
  The associated contact.
### Getting the Property Information
- [var key: String](./cncontactproperty/key.md)
  The key of the contact property.
- [var value: Any?](./cncontactproperty/value.md)
  The value of the property.
- [var label: String?](./cncontactproperty/label.md)
  The label of the labeled value of the property array.
- [var identifier: String?](./cncontactproperty/identifier.md)
  The identifier of the labeled value in the array of labeled.
### Handling Exceptions
- [let CNContactPropertyNotFetchedExceptionName: String](./cncontactpropertynotfetchedexceptionname.md)
  Exception thrown when an accessed property was not fetched.
### Initializers
- [init?(coder: NSCoder)](./cncontactproperty/init%28coder%29.md)

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

## See Also

### Generic Types
- [class CNLabeledValue](./cnlabeledvalue.md)
  An immutable object that combines a contact property value with a label that describes that property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty)*