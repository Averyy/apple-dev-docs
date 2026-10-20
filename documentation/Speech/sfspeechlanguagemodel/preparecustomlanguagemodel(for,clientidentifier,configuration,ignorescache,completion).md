# prepareCustomLanguageModel(for:clientIdentifier:configuration:ignoresCache:completion:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 17.0+ - Deprecated in 26.0
- iPadOS 17.0+ - Deprecated in 26.0
- Mac Catalyst 17.0+ - Deprecated in 26.0
- macOS 14.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
class func prepareCustomLanguageModel(for asset: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func prepareCustomLanguageModel(for asset: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, ignoresCache: Bool) async throws
```

```objc
+ (void) prepareCustomLanguageModelForUrl:(NSURL *) asset clientIdentifier:(NSString *) clientIdentifier configuration:(SFSpeechLanguageModelConfiguration *) configuration ignoresCache:(BOOL) ignoresCache completion:(void (^)(NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/preparecustomlanguagemodel(for:clientidentifier:configuration:ignorescache:completion:))*