# entriesEnumeratorAndReturnError:

**Framework**: OSLog  
**Kind**: method  
**Role**: Instance Method

Returns a log enumerator with default options for viewing the entries.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (OSLogEnumerator *) entriesEnumeratorAndReturnError:(NSError **) error;
```

## Discussion

This method returns all of the entries from earliest to latest. If the enumerator can’t be set up, `entriesEnumeratorAndReturnError` returns `nil` and sets the error parameter to an error object describing the problem.

## See Also

### Accessing Entries
- [- entriesEnumeratorWithOptions:position:predicate:error:](./entriesenumeratorwithoptions_position_predicate_error_.md)
  Returns a log enumerator based on an underlying store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/entriesenumeratorandreturnerror:)*