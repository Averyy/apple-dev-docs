# init(contentsOfFile:byReference:)

**Framework**: AppKit  
**Kind**: init

Initializes the receiver with the audio data located at a given filepath.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(contentsOfFile path: String, byReference byRef: Bool)
```

#### Return Value

Initialized `NSSound` instance.

## Parameters

- `path`: Path to the sound file with which the receiver is to be initialized.
- `byRef`: When [`true`](https://developer.apple.com/documentation/swift/true) only the name of the sound is stored with the `NSSound` instance when archived using [`encode(with:)`](https://developer.apple.com/documentation/foundation/nscoding/encode(with:)); otherwise the audio data is archived along with the instance.

## See Also

- [class func canInit(with: NSPasteboard) -> Bool](nssound/caninit(with:).md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOf: URL, byReference: Bool)](nssound/init(contentsof:byreference:).md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](nssound/init(data:).md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](nssound/init(pasteboard:).md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/init(contentsoffile:byreference:))*