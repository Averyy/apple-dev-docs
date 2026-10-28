# loadBroadcastingApplicationInfo(completion:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadBroadcastingApplicationInfo(completion handler: @escaping @Sendable (String, String, UIImage?) -> Void)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadBroadcastingApplicationInfo() async -> (String, String, UIImage?)
```

*macOS*

```swift
func loadBroadcastingApplicationInfo(completion handler: @escaping @Sendable (String, String, NSImage?) -> Void)
```

*macOS*

```swift
func loadBroadcastingApplicationInfo() async -> (String, String, NSImage?)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) loadBroadcastingApplicationInfoWithCompletion:(void (^)(NSString *bundleID, NSString *displayName, UIImage *appIcon)) handler;
```

*macOS*

```objc
- (void) loadBroadcastingApplicationInfoWithCompletion:(void (^)(NSString *bundleID, NSString *displayName, NSImage *appIcon)) handler;
```

## Discussion

## See Also

### Supporting broadcasting
- [func completeRequest(withBroadcast: URL, setupInfo: [String : any NSCoding & NSObjectProtocol]?)](./completerequest%28withbroadcast,setupinfo%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/loadbroadcastingapplicationinfo(completion:))*