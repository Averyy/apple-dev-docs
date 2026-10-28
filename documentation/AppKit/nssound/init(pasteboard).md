# init(pasteboard:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](../nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.

**Availability**:
- macOS

## Declaration

```swift
init?(pasteboard: NSPasteboard)
```

```objc
- (instancetype) initWithPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

Initialized `NSSound` instance.

## Parameters

- `pasteboard`: The pasteboard containing the audio data with which the receiver is to be initialized. The pasteboard must contain a type returned by [`NSSound`](../nssound.md). The contained data must have a proper magic number, sound header, and data for the formats the `NSSound` class supports.

## See Also

### Creating Sounds
- [class func canInit(with: NSPasteboard) -> Bool](./caninit%28with%29.md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOfFile: String, byReference: Bool)](./init%28contentsoffile,byreference%29.md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](./init%28contentsof,byreference%29.md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](./init%28data%29.md)
  Initializes the receiver with a given audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/init(pasteboard:))*