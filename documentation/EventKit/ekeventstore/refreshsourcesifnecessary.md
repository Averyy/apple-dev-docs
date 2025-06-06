# refreshSourcesIfNecessary()

**Framework**: EventKit  
**Kind**: method

Pulls new data from remote sources, if necessary.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func refreshSourcesIfNecessary()
```

#### Discussion

Use this method to pull new data from remote sources if the local data is out of date.

## See Also

- [func commit() throws](ekeventstore/commit.md)
  Commits all unsaved changes to the event store.
- [func reset()](ekeventstore/reset.md)
  Reverts the event store to its saved state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/refreshsourcesifnecessary())*