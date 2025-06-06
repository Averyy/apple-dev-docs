# init(pasteboard:)

**Framework**: AppKit  
**Kind**: init

Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(pasteboard: NSPasteboard)
```

#### Return Value

Initialized `NSSound` instance.

## Parameters

- `pasteboard`: The pasteboard containing the audio data with which the receiver is to be initialized. The pasteboard must contain a type returned by  . The contained data must have a proper magic number, sound header, and data for the formats the   class supports.

## See Also

- [class func canInit(with: NSPasteboard) -> Bool](nssound/caninit(with:).md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOfFile: String, byReference: Bool)](nssound/init(contentsoffile:byreference:).md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](nssound/init(contentsof:byreference:).md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](nssound/init(data:).md)
  Initializes the receiver with a given audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/init(pasteboard:))*