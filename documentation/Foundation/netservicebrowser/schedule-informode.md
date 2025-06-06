# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method

Adds the receiver to the specified run loop.

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

You can use this method in conjunction with [`remove(from:forMode:)`](netservicebrowser/remove(from:formode:).md) to transfer the receiver to a run loop other than the default one. You should not attempt to run the receiver on multiple run loops.

## Parameters

- `aRunLoop`: Run loop in which to schedule the receiver.
- `mode`: Run loop mode in which to perform this operation, such as  . See the Run Loop Modes section of the   class for other run loop mode values.

## See Also

- [func remove(from: RunLoop, forMode: RunLoop.Mode)](netservicebrowser/remove(from:formode:).md)
  Removes the receiver from the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/schedule(in:formode:))*