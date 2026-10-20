# download(withCompletionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.13+

## Declaration

```swift
func download(withCompletionHandler completionHandler: @escaping ((any Error)?) -> Bool)
```

```objc
- (void) downloadFontAssetsWithCompletionHandler:(BOOL (^)(NSError *error)) completionHandler;
```

## See Also

### Downloading a Font Asset
- [var downloadedFontDescriptors: [NSFontDescriptor]](./downloadedfontdescriptors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontassetrequest/download(withcompletionhandler:))*