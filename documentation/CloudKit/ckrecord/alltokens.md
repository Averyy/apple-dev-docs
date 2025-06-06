# allTokens()

**Framework**: CloudKit  
**Kind**: method

Returns an array of strings to use for full-text searches of the field’s string-based values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func allTokens() -> [String]
```

#### Return Value

An array of strings that contains data from the record’s string-based fields.

#### Discussion

When performing your own full-text searches, you can use this method to get a list of strings for your search. The method acts only on keys with string values. It breaks each value string apart at whitespace boundaries, creates new strings for each word, adds the new strings to an array, and returns the array. This tokenized version of the record’s string values makes it easier to do string-based comparisons of individual words.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/alltokens())*