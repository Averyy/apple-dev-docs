# suggestionType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of contact information to donate with interactions.

## Declaration

```swift
var suggestionType: INPersonSuggestionType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INPersonSuggestionType suggestionType;
```

*macOS*

```objc
@property (atomic, readonly) INPersonSuggestionType suggestionType;
```

## Discussion

When donating interactions involving a person, the system uses this property to determine how to surface the user’s identity. For example, an app might prefer to display the person’s social media profile name rather than their real name.

If you use the [`init(personHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:)`](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier%29.md) method to create the person object, interactions reflect the person’s name, instead of the name of a social media or instant messaging account.

## See Also

### Accessing suggestion details
- [var isContactSuggestion: Bool](./iscontactsuggestion.md)
  A Boolean value that indicates whether the person is a contact suggestion.
- [enum INPersonSuggestionType](../inpersonsuggestiontype.md)
  Constants indicating how to display the person’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/suggestiontype)*