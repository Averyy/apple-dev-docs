# reset()

**Framework**: EventKit  
**Kind**: method

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

#### Discussion

This method updates all the properties of all the objects with their corresponding values in the event store. Any local changes that aren’t saved before invoking this method are lost. All existing objects created or retrieved using this store are disassociated from it and are invalid.

## See Also

- [func commit() throws](ekeventstore/commit.md)
  Commits all unsaved changes to the event store.
- [func refreshSourcesIfNecessary()](ekeventstore/refreshsourcesifnecessary.md)
  Pulls new data from remote sources, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/reset())*