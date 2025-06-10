# PermissionChoice

**Framework**: PermissionKit  
**Kind**: struct

A class that uniquely identifies a specific, statically defined permission choice.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct PermissionChoice
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

#### Overview

Each PermissionQuestion contains a set of possible answer choices, each corresponding to a globally unique identifier that you can interpret. If your application only requires a yes or no response, you can use the two predefined PermissionChoice options: Approve and Decline.

```swift
public static let approve: PermissionChoice
public static let decline: PermissionChoice
```

## Topics

### Determining the permission choice
- [var answer: PermissionChoice.Answer](permissionchoice/answer-swift.property.md)
  The kind of answer this choice is. The system will use this to properly stylize the choice when displaying it to the user.
- [PermissionChoice.Answer](permissionchoice/answer-swift.enum.md)
  An answer to the permission request.
- [static let approve: PermissionChoice](permissionchoice/approve.md)
  The system-preferred choice to approve a permission request.
- [static let decline: PermissionChoice](permissionchoice/decline.md)
  The system-preferred choice to decline a permission request.
### Identifying the permission
- [var id: String](permissionchoice/id-swift.property.md)
  A unique identifier for this choice.
- [var title: String](permissionchoice/title.md)
  The title for this choice that will be displayed to the user by the system.
### Decoding
- [init(from: any Decoder) throws](permissionchoice/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Performing hashes
- [func hash(into: inout Hasher)](permissionchoice/hash(into:).md)
  Performs a hash operation on the value by feeding its hash values into the given hasher.
### Operators
- [static func == (PermissionChoice, PermissionChoice) -> Bool](permissionchoice/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](permissionchoice/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](permissionchoice/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [PermissionChoice.ID](permissionchoice/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](permissionchoice/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [protocol QuestionTopic](questiontopic.md)
  A protocol that defines a question topic that can be used to interpret what a user is asking for.
- [class PermissionQuestion](permissionquestion.md)
  A class that captures a permission question posed by a user.
- [struct CommunicationTopic](communicationtopic.md)
  A question topic related to communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionchoice)*