# INPersonRelationship

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants indicating the relationship between the person using the device and another person.

## Declaration

```swift
struct INPersonRelationship
```

```c
typedef NSString * INPersonRelationship;
```

## Topics

### Relationship Type
- [static let assistant: INPersonRelationship](./inpersonrelationship/assistant.md)
  The person is an assistant to the current user.
- [static let brother: INPersonRelationship](./inpersonrelationship/brother.md)
  The person is the brother of the current user.
- [static let child: INPersonRelationship](./inpersonrelationship/child.md)
  The person is a child of the current user.
- [static let father: INPersonRelationship](./inpersonrelationship/father.md)
  The person is the father of the current user.
- [static let friend: INPersonRelationship](./inpersonrelationship/friend.md)
  The person is a friend of the current user.
- [static let manager: INPersonRelationship](./inpersonrelationship/manager.md)
  The person is the manager of the current user.
- [static let mother: INPersonRelationship](./inpersonrelationship/mother.md)
  The person is the mother of the current user.
- [static let parent: INPersonRelationship](./inpersonrelationship/parent.md)
  The person is a parent of the current user.
- [static let partner: INPersonRelationship](./inpersonrelationship/partner.md)
  The person is the partner of the current user.
- [static let sister: INPersonRelationship](./inpersonrelationship/sister.md)
  The person is the sister of the current user.
- [static let spouse: INPersonRelationship](./inpersonrelationship/spouse.md)
  The person is the spouse of the current user.
- [static let daughter: INPersonRelationship](./inpersonrelationship/daughter.md)
  The person is the daughter of the current user.
- [static let son: INPersonRelationship](./inpersonrelationship/son.md)
  The person is the son of the current user.
### Initializers
- [init(String)](./inpersonrelationship/init%28_%29.md)
  Creates a person relationship type with the specified raw value.
- [init(rawValue: String)](./inpersonrelationship/init%28rawvalue%29.md)
  Creates a person relationship type with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing relationship details
- [var relationship: INPersonRelationship?](./inperson/relationship.md)
  The relationship between this person and the person using the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonrelationship)*