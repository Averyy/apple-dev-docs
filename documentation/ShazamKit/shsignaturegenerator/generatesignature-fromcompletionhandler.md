# generateSignature(from:completionHandler:)

**Framework**: ShazamKit  
**Kind**: method

Creates a signature with the asset you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func signature(from asset: AVAsset) async throws -> SHSignature
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func signature(from asset: AVAsset) async throws -> SHSignature
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func signature(from asset: AVAsset) async throws -> SHSignature
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The asset you specify can be any type of media that contains audio tracks. If the asset has multiple tracks, the system mixes them into one [`SHSignature`](shsignature.md).

## Parameters

- `asset`: An asset that contains the audio to convert.
- `completionHandler`: This block takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignaturegenerator/generatesignature(from:completionhandler:))*