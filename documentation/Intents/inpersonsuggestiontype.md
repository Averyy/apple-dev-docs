# INPersonSuggestionType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how to display the person’s identity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INPersonSuggestionType
```

```c
enum INPersonSuggestionType : NSInteger;
```

## Topics

### Constants
- [INPersonSuggestionType.none](./inpersonsuggestiontype/none.md)
  No contact information to donate.
- [INPersonSuggestionType.socialProfile](./inpersonsuggestiontype/socialprofile.md)
  A social media account.
- [INPersonSuggestionType.instantMessageAddress](./inpersonsuggestiontype/instantmessageaddress.md)
  An instant messaging address.
### Initializers
- [init?(rawValue: Int)](./inpersonsuggestiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing suggestion details
- [var isContactSuggestion: Bool](./inperson/iscontactsuggestion.md)
  A Boolean value that indicates whether the person is a contact suggestion.
- [var suggestionType: INPersonSuggestionType](./inperson/suggestiontype.md)
  The type of contact information to donate with interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonsuggestiontype)*