# enable

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Enables collection after collection has been disabled.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) enable;
```

## Discussion

This method balances a single invocation of [`disable`](./disable.md). To reenable collection, this method must be invoked as many times as was [`disable`](./disable.md).

## See Also

### Collection State
- [- disable](./disable.md)
  Temporarily disables collections.
- [- isEnabled](./isenabled.md)
  Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process.
- [- isCollecting](./iscollecting.md)
  Returns a Boolean value that indicates whether a collection is currently in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/enable)*