# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts a tag for each token in the specified array.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func prediction(from tokens: [MLWordTagger.Token]) throws -> [String]
```

**Other overloads**:

```swift
func prediction(from text: String) throws -> [String]
```

## Return Value

An array of tags for the tokens.

## Parameters

- `tokens`: An array of tokens to tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/prediction(from:)-7rqyq)*