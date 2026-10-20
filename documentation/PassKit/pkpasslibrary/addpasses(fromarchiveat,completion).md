# addPasses(fromArchiveAt:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
func addPasses(fromArchiveAt passesArchiveFileURL: URL, completion completionHandler: @escaping @Sendable (PKPassLibraryAddPassesStatus) -> Void)
```

```swift
func addPasses(fromArchiveAt passesArchiveFileURL: URL) async -> PKPassLibraryAddPassesStatus
```

```objc
- (void) addPassesFromArchiveAtFileURL:(NSURL *) passesArchiveFileURL completionHandler:(void (^)(PKPassLibraryAddPassesStatus )) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/addpasses(fromarchiveat:completion:))*