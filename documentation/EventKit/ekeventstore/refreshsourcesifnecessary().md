# refreshSourcesIfNecessary()

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) refreshSourcesIfNecessary;
```

#### Discussion

Use this method to pull new data from remote sources if the local data is out of date.

## See Also

### Saving and restoring state
- [func commit() throws](./commit%28%29.md)
  Commits all unsaved changes to the event store.
- [func reset()](./reset%28%29.md)
  Reverts the event store to its saved state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/refreshsourcesifnecessary())*