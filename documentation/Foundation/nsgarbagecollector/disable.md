# disable

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Temporarily disables collections.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) disable;
```

## Discussion

Invocations of this method can be nested. To reenable collection, you must send the collector an [`enable`](./enable.md) message once for each invocation of this method.

## See Also

### Collection State
- [- enable](./enable.md)
  Enables collection after collection has been disabled.
- [- isEnabled](./isenabled.md)
  Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process.
- [- isCollecting](./iscollecting.md)
  Returns a Boolean value that indicates whether a collection is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/disable)*