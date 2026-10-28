# defaultCollector

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the default garbage collector.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
+ (id) defaultCollector;
```

## Return Value

The default garbage collector for the current process. Returns `nil` if the current process is not running with garbage collection.

## Discussion

There is at most one garbage collector for Cocoa within a single process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/defaultcollector)*