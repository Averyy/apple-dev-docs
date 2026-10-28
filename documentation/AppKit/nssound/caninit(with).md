# canInit(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Indicates whether the receiver can create an instance of itself from the data in a pasteboard.

**Availability**:
- macOS

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

```objc
+ (BOOL) canInitWithPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

[`true`](../../Swift/true.md) when the receiver can handle the data represented by `pasteboard`; [`false`](../../Swift/false.md) otherwise.

## Discussion

The [`NSSound`](../nssound.md) method is used to find out whether the class can handle the data in `pasteboard`.

## Parameters

- `pasteboard`: Pasteboard containing sound data.

## See Also

### Related Documentation
- [Sound Programming Topics for Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Sound.html#//apple_ref/doc/uid/10000104i)
### Creating Sounds
- [init?(contentsOfFile: String, byReference: Bool)](./init%28contentsoffile,byreference%29.md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](./init%28contentsof,byreference%29.md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](./init%28data%29.md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](../nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/caninit(with:))*