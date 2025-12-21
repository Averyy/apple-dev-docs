# SHSession

**Framework**: ShazamKit  
**Kind**: class

An object that matches a specific audio recording when a segment of that recording is part of captured sound in the Shazam catalog or your custom catalog.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class SHSession
```

## Mentions

- [Matching audio using the built-in microphone](matching-audio-using-the-built-in-microphone.md)

#### Overview

Prepare to make matches by:

- Creating a session for the catalog that contains the reference signatures
- Adding your delegate that receives the match results

Search for a match in one of two ways:

- Generate a signature for the captured audio and call [`match(_:)`](shsession/match(_:).md)
- Call [`matchStreamingBuffer(_:at:)`](shsession/matchstreamingbuffer(_:at:).md) with a streaming audio buffer, and ShazamKit generates the signature for you

Searching the catalog is asynchronous. The session calls your delegate methods with the result.

Matching songs in Shazam music requires enabling your app to access the catalog. For more information on enabling your app, see [`Enable ShazamKit for an App ID`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-services/shazamkit).

The code below shows searching for a match in the Shazam catalog using an existing audio buffer:

```swift
// Set up the session.
let session = SHSession()

// Create a signature from the captured audio buffer.
let signatureGenerator = SHSignatureGenerator()
try signatureGenerator.append(buffer, at: audioTime)
let signature = signatureGenerator.signature()

// Check for a match.
let result = await session.result(from: signature)

// Use the result.
switch result {
 case .match(let match):
      // Match found.
 case .noMatch(let signature):
      // No match found.
 case .error(let error, let signature):
      // An error occurred.
}
```

## Topics

### Creating a session object
- [init()](shsession/init.md)
  Creates a new session object for matching songs in the Shazam Music catalog.
- [init(catalog: SHCatalog)](shsession/init(catalog:).md)
  Creates a new session object for matching audio in a custom catalog.
### Making a match
- [func match(SHSignature)](shsession/match(_:).md)
  Searches for the query signature in the reference signatures that the session catalog contains.
- [func matchStreamingBuffer(AVAudioPCMBuffer, at: AVAudioTime?)](shsession/matchstreamingbuffer(_:at:).md)
  Converts the audio in the buffer to a signature, and searches the reference signatures in the session catalog.
- [Matching audio using the built-in microphone](matching-audio-using-the-built-in-microphone.md)
  Use the audio stream from the microphone as the source for a ShazamKit session.
### Reading the session properties
- [var delegate: (any SHSessionDelegate)?](shsession/delegate.md)
  The object that the session calls with the result of a match request.
- [var catalog: SHCatalog](shsession/catalog.md)
  The catalog object containing the reference signatures and their associated metadata that the session uses to perform matches.
- [var results: SHSession.Results](shsession/results-swift.property.md)
  The results as an asynchronous sequence of matches.
- [SHSession.Results](shsession/results-swift.struct.md)
  An asynchronous sequence that emits updates from a session object query.
### Returning queries
- [func result(from: SHSignature) async -> SHSession.Result](shsession/result(from:).md)
  Performs an asynchronous match with a signature you specify.
- [SHSession.Result](shsession/result.md)
  Identifies the result from an asynchronous sequence result.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SHManagedSession](shmanagedsession.md)
  An object that records and matches a recording with captured sound in the Shazam catalog or your custom catalog.
- [protocol SHSessionDelegate](shsessiondelegate.md)
  Methods that the session calls with the result of a match request.
- [class SHMatch](shmatch.md)
  An object that represents the catalog media items that match a query.
- [class SHMatchedMediaItem](shmatchedmediaitem.md)
  An object that represents the metadata for a matched reference signature.
- [class SHMediaItem](shmediaitem.md)
  An object that represents the metadata for a reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsession)*