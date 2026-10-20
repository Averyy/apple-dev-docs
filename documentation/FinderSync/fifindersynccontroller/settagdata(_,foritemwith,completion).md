# setTagData(_:forItemWith:completion:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setTagData(_ tagData: Data?, forItemWith itemURL: URL, completion: @escaping @Sendable (any Error) -> Void)
```

```swift
func setTagData(_ tagData: Data?, forItemWith itemURL: URL) async -> any Error
```

```objc
- (void) setTagData:(NSData *) tagData forItemWithURL:(NSURL *) itemURL completion:(void (^)(NSError *error)) completion;
```

#### Overview

> **Concurrency Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func setTagData(_ tagData: Data?, forItemWith itemURL: URL) async -> Error
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/settagdata(_:foritemwith:completion:))*