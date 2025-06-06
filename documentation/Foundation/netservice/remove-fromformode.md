# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method

Removes the service from the given run loop for a given mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

You can use this method in conjunction with [`schedule(in:forMode:)`](netservice/schedule(in:formode:).md) to transfer the service to a different run loop. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, it is an error to do so.

## Parameters

- `aRunLoop`: The run loop from which to remove the receiver.
- `mode`: The run loop mode from which to remove the receiver. Possible values for   are discussed in the “Constants” section of  .

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](netservice/schedule(in:formode:).md)
  Adds the service to the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/remove(from:formode:))*