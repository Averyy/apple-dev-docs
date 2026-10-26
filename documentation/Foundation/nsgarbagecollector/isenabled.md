# isEnabled

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (BOOL) isEnabled;
```

#### Return Value

[`true`](../../Swift/true.md) if garbage collection is enabled for the current process, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method returns [`false`](../../Swift/false.md) if garbage collection is on, but has been temporarily suspended (using [`disable`](./disable.md)).

To check whether the current process is using garbage collection check the result of `[NSGarbageCollector defaultCollector]`. If [`defaultCollector`](./defaultcollector.md) is `nil`, then garbage collection is permanently off. If [`defaultCollector`](./defaultcollector.md) is not `nil`, then the current process is using garbage collection—you can then use `isEnabled` to determine whether or not the collector is actually allowed to run right now.

## See Also

### Collection State
- [- disable](./disable.md)
  Temporarily disables collections.
- [- enable](./enable.md)
  Enables collection after collection has been disabled.
- [- isCollecting](./iscollecting.md)
  Returns a Boolean value that indicates whether a collection is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/isenabled)*