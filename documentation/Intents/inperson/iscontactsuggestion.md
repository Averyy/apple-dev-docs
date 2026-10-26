# isContactSuggestion

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the person is a contact suggestion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isContactSuggestion: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isContactSuggestion) BOOL contactSuggestion;
```

*macOS*

```objc
@property (atomic, readonly, getter=isContactSuggestion) BOOL contactSuggestion;
```

## See Also

### Accessing suggestion details
- [var suggestionType: INPersonSuggestionType](./suggestiontype.md)
  The type of contact information to donate with interactions.
- [enum INPersonSuggestionType](../inpersonsuggestiontype.md)
  Constants indicating how to display the person’s identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/iscontactsuggestion)*