# entriesEnumeratorWithOptions:position:predicate:error:

**Framework**: OSLog  
**Kind**: method  
**Role**: Instance Method

Returns a log enumerator based on an underlying store.

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
- (OSLogEnumerator *) entriesEnumeratorWithOptions:(OSLogEnumeratorOptions) options position:(OSLogPosition *) position predicate:(NSPredicate *) predicate error:(NSError **) error;
```

## Discussion

The returned object represents the sequence of entries for the `OSLogStore`. Use the additional parameters to control which entries are returned and their order.

## See Also

### Accessing Entries
- [- entriesEnumeratorAndReturnError:](./entriesenumeratorandreturnerror_.md)
  Returns a log enumerator with default options for viewing the entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/entriesenumeratorwithoptions:position:predicate:error:)*