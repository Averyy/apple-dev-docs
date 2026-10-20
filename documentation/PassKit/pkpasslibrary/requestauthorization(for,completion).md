# requestAuthorization(for:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Requests a person’s authorization to use a pass library capability.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requestAuthorization(for capability: PKPassLibrary.Capability, completion: @escaping @Sendable (PKPassLibrary.AuthorizationStatus) -> Void)
```

```swift
func requestAuthorization(for capability: PKPassLibrary.Capability) async -> PKPassLibrary.AuthorizationStatus
```

```objc
- (void) requestAuthorizationForCapability:(PKPassLibraryCapability) capability completion:(void (^)(PKPassLibraryAuthorizationStatus status)) completion;
```

#### Discussion

Call this method before using a capability that requires someone’s explicit permission, like [`PKPassLibrary.Capability.backgroundAddPasses`](./capability/backgroundaddpasses.md). If the person hasn’t decided whether to grant your app that capability, PassKit prompts them for permission and calls your completion handler with their choice. If the person already granted or denied the capability, PassKit calls your completion handler immediately, without showing a prompt.

Use [`authorizationStatus(for:)`](./authorizationstatus%28for%29.md) to check the person’s current authorization status for a capability without prompting them.

## See Also

### Automatically adding passes
- [PKPassLibrary.AuthorizationStatus](./authorizationstatus.md)
  Statuses that indicate whether a person authorized your app to add a pass to their Wallet.
- [PKPassLibrary.Capability](./capability.md)
  Features for which your app can request authorization from a person.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/requestauthorization(for:completion:))*