# pipe

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSPipe` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSPipe *) pipe;
```

## Return Value

An initialized `NSPipe` object. Returns `nil` if the method encounters errors while attempting to create the pipe or the `NSFileHandle` objects that serve as endpoints of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspipe/pipe)*