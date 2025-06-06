# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method

Adds the service to the specified run loop.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

You can use this method in conjunction with [`remove(from:forMode:)`](netservice/remove(from:formode:).md) to transfer a service to a different run loop. You should not attempt to run a service on multiple run loops.

## Parameters

- `aRunLoop`: The run loop to which to add the receiver.
- `mode`: The run loop mode to which to add the receiver. Possible values for   are discussed in the “Constants” section of  .

## See Also

- [func remove(from: RunLoop, forMode: RunLoop.Mode)](netservice/remove(from:formode:).md)
  Removes the service from the given run loop for a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/schedule(in:formode:))*