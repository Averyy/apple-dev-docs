# setLastUsedDate(_:forItemWith:completion:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setLastUsedDate(_ lastUsedDate: Date, forItemWith itemURL: URL, completion: @escaping @Sendable (any Error) -> Void)
```

```swift
func setLastUsedDate(_ lastUsedDate: Date, forItemWith itemURL: URL) async -> any Error
```

```objc
- (void) setLastUsedDate:(NSDate *) lastUsedDate forItemWithURL:(NSURL *) itemURL completion:(void (^)(NSError *error)) completion;
```

#### Overview

> **Concurrency Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func setLastUsedDate(_ lastUsedDate: Date, forItemWith itemURL: URL) async -> Error
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller/setlastuseddate(_:foritemwith:completion:))*