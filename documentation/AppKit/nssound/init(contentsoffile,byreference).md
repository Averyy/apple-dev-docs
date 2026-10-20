# init(contentsOfFile:byReference:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with the audio data located at a given filepath.

**Availability**:
- macOS

## Declaration

```swift
init?(contentsOfFile path: String, byReference byRef: Bool)
```

```objc
- (instancetype) initWithContentsOfFile:(NSString *) path byReference:(BOOL) byRef;
```

#### Return Value

Initialized `NSSound` instance.

## Parameters

- `path`: Path to the sound file with which the receiver is to be initialized.
- `byRef`: When [`true`](../../Swift/true.md) only the name of the sound is stored with the `NSSound` instance when archived using [`encode(with:)`](../../Foundation/nscoding/encode%28with%29.md); otherwise the audio data is archived along with the instance.

## See Also

### Creating Sounds
- [class func canInit(with: NSPasteboard) -> Bool](./caninit%28with%29.md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOf: URL, byReference: Bool)](./init%28contentsof,byreference%29.md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](./init%28data%29.md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](../nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/init(contentsoffile:byreference:))*