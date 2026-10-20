# executionTime(for:atTime:withArguments:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func executionTime(for context: (any QCPlugInContext)!, atTime time: TimeInterval, withArguments arguments: [AnyHashable : Any]!) -> TimeInterval
```

```objc
- (NSTimeInterval) executionTimeForContext:(id<QCPlugInContext>) context atTime:(NSTimeInterval) time withArguments:(NSDictionary *) arguments;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/executiontime(for:attime:witharguments:))*