# collectIfNeeded

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver to collect if memory consumption thresholds have been exceeded.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) collectIfNeeded;
```

## Discussion

You use this method to indicate to the collector that there is an opportunity to perform a collection. Collection is subject to interruption on user input.

## See Also

### Triggering Collection
- [- collectExhaustively](./collectexhaustively.md)
  Tells the receiver to collect iteratively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/collectifneeded)*