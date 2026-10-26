# collectExhaustively

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver to collect iteratively.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) collectExhaustively;
```

#### Discussion

You use this method to indicate to the collector that it should perform an exhaustive collection. Collection is subject to interruption on user input.

## See Also

### Triggering Collection
- [- collectIfNeeded](./collectifneeded.md)
  Tells the receiver to collect if memory consumption thresholds have been exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/collectexhaustively)*