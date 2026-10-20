# fetchCurrentDownloads()

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func fetchCurrentDownloads() throws -> [BADownload]
```

```objc
- (NSArray<BADownload *> *) fetchCurrentDownloads:(NSError **) error;
```

## See Also

### Fetching in-progress downloads
- [func fetchCurrentDownloads(completionHandler: ([BADownload], (any Error)?) -> Void)](./fetchcurrentdownloads%28completionhandler%29.md)
  Fetches the contents of the manager’s download queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/fetchcurrentdownloads())*