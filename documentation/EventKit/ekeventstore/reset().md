# reset()

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Reverts the event store to its saved state.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

## Discussion

This method updates all the properties of all the objects with their corresponding values in the event store. Any local changes that aren’t saved before invoking this method are lost. All existing objects created or retrieved using this store are disassociated from it and are invalid.

## See Also

### Saving and restoring state
- [func commit() throws](./commit%28%29.md)
  Commits all unsaved changes to the event store.
- [func refreshSourcesIfNecessary()](./refreshsourcesifnecessary%28%29.md)
  Pulls new data from remote sources, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/reset())*