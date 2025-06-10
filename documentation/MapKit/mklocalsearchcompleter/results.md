# results

**Framework**: MapKit  
**Kind**: property

The most recently received search completions.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var results: [MKLocalSearchCompletion] { get }
```

#### Discussion

This property is `nil` initially. After a successful query, the search completer sets this property to the array of [`MKLocalSearchCompletion`](mklocalsearchcompletion.md) objects that the query returns. Each new successful query replaces the previous value of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/results)*