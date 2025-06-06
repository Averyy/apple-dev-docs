# init(currentSuggestion:)

**Framework**: Core Spotlight  
**Kind**: init

Creates a new query context object with an optional suggested search string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(currentSuggestion: CSSuggestion?)
```

#### Return Value

An initialized user query context object. Configure the properties of the returned object and use it to construct a [`CSUserQuery`](csuserquery.md) object.

## Parameters

- `currentSuggestion`: The suggested text completion that the person   selected in your interface. Specify   if the person hasn’t   chosen a suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquerycontext/init(currentsuggestion:))*