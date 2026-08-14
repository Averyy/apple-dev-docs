# CLKWatchFaceLibrary

**Framework**: ClockKit  
**Kind**: class

An object for importing watch faces that the app provides.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.0+

## Declaration

```swift
class CLKWatchFaceLibrary
```

## Mentions

- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)

#### Overview

Use a [`CLKWatchFaceLibrary`](clkwatchfacelibrary.md) object to add an existing .`watchface` file to the Watch app. Add watch faces only on devices that support pairing with an Apple Watch.

## Topics

### Importing a Watch Face
- [func addWatchFace(at: URL, completionHandler: ((any Error)?) -> Void)](clkwatchfacelibrary/addwatchface(at:completionhandler:).md)
  Adds a watch face from the app’s bundle.
### Handling Errors
- [class let ErrorDomain: String](clkwatchfacelibrary/errordomain.md)
  The domain for errors while importing watch faces.
- [CLKWatchFaceLibrary.ErrorCode](clkwatchfacelibrary/errorcode.md)
  Error codes that the watch face library returns.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Sharing an Apple Watch face](sharing-an-apple-watch-face.md)
  Distribute a customized watch face to Apple Watch users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkwatchfacelibrary)*