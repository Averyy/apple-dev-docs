# withExclusiveControl(beforeDate:perform:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 27.0
- iPadOS 16.1+ - Deprecated in 27.0
- Mac Catalyst 16.1+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.0
- tvOS 18.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

> **Deprecated**: Use withExclusiveControl(before:_:) instead.

## Declaration

```swift
func withExclusiveControl(beforeDate date: Date, perform performHandler: @escaping (Bool, (any Error)?) -> Void)
```

```objc
- (void) performWithExclusiveControlBeforeDate:(NSDate *) date performHandler:(void (^)(BOOL acquiredLock, NSError *error)) performHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(beforedate:perform:))*