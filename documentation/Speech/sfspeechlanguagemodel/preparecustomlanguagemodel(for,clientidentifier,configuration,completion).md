# prepareCustomLanguageModel(for:clientIdentifier:configuration:completion:)

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
class func prepareCustomLanguageModel(for asset: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func prepareCustomLanguageModel(for asset: URL, clientIdentifier: String, configuration: SFSpeechLanguageModel.Configuration) async throws
```

```objc
+ (void) prepareCustomLanguageModelForUrl:(NSURL *) asset clientIdentifier:(NSString *) clientIdentifier configuration:(SFSpeechLanguageModelConfiguration *) configuration completion:(void (^)(NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/preparecustomlanguagemodel(for:clientidentifier:configuration:completion:))*