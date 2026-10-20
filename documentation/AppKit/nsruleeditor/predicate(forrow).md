# predicate(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the predicate for a given row.

**Availability**:
- macOS

## Declaration

```swift
func predicate(forRow row: Int) -> NSPredicate?
```

```objc
- (NSPredicate *) predicateForRow:(NSInteger) row;
```

#### Return Value

The predicate for the row at `row`.

#### Discussion

You should rarely have a need to call this directly, but you can override this method in a subclass to perform specialized predicate handling for certain criteria or display values.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

### Working with Predicates
- [var predicate: NSPredicate?](./predicate.md)
  The rule editor’s predicate.
- [func reloadPredicate()](./reloadpredicate%28%29.md)
  Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/predicate(forrow:))*