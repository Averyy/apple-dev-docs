# canInit(with:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the receiver can create an instance of itself from the data in a pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when the receiver can handle the data represented by `pasteboard`; [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The [`NSSound`](nssound.md) method is used to find out whether the class can handle the data in `pasteboard`.

## Parameters

- `pasteboard`: Pasteboard containing sound data.

## See Also

- [Sound Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Sound.html#//apple_ref/doc/uid/10000104i)
- [init?(contentsOfFile: String, byReference: Bool)](nssound/init(contentsoffile:byreference:).md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](nssound/init(contentsof:byreference:).md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](nssound/init(data:).md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](nssound/init(pasteboard:).md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/caninit(with:))*