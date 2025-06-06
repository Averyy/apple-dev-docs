# withExclusiveControl(beforeDate:perform:)

**Framework**: Background Assets  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func withExclusiveControl(beforeDate date: Date, perform performHandler: @escaping (Bool, (any Error)?) -> Void)
```

## See Also

- [func withExclusiveControl((Bool, (any Error)?) -> Void)](badownloadmanager/withexclusivecontrol(_:).md)
  Attempts to acquire immediate, exclusive access to the download manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/withexclusivecontrol(beforedate:perform:))*