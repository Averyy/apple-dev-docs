# criteria

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The information to use when performing the search.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
var criteria: Self.Criteria { get set }
```

#### Discussion

Use this property to get the search terms or other criteria to use when you perform a search. You specify the search criteria you support when you define your custom type. For example, set the type of this property to [`StringSearchCriteria`](stringsearchcriteria.md) to match items against a string value.

## See Also

- [protocol SearchCriteria](searchcriteria.md)
  An interface for defining the criteria to use when searching your app’s content.
- [struct StringSearchCriteria](stringsearchcriteria.md)
  A type that tells your app to match its items against a provided string.
- [associatedtype Criteria : SearchCriteria](showinappsearchresultsintent/criteria-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/showinappsearchresultsintent/criteria-swift.property)*