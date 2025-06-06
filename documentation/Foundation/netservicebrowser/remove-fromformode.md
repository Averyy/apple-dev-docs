# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method

Removes the receiver from the specified run loop.

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

You can use this method in conjunction with [`schedule(in:forMode:)`](netservicebrowser/schedule(in:formode:).md) to transfer the receiver to a run loop other than the default one. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, you must not do it.

## Parameters

- `aRunLoop`: Run loop from which to remove the receiver.
- `mode`: Run loop mode in which to perform this operation, such as  . See the Run Loop Modes section of the   class for other run loop mode values.

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](netservicebrowser/schedule(in:formode:).md)
  Adds the receiver to the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/remove(from:formode:))*