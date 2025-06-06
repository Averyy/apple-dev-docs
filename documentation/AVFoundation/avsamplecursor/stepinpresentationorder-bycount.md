# stepInPresentationOrder(byCount:)

**Framework**: AVFoundation  
**Kind**: method

Moves the cursor a given number of samples in presentation order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func stepInPresentationOrder(byCount stepCount: Int64) -> Int64
```

#### Return Value

The number of samples the cursor traversed. If the cursor reaches the beginning or the end of the sample sequence before the requested number of samples was traversed, the absolute value of the result will be less than the absolute value of the specified step count.

## Parameters

- `stepCount`: The number of samples to move across. If positive, step forward this many samples. If negative, step backward this many samples.

## See Also

- [func step(byDecodeTime: CMTime, wasPinned: UnsafeMutablePointer<ObjCBool>?) -> CMTime](avsamplecursor/step(bydecodetime:waspinned:).md)
  Moves the cursor by a given delta time on the decode timeline.
- [func step(byPresentationTime: CMTime, wasPinned: UnsafeMutablePointer<ObjCBool>?) -> CMTime](avsamplecursor/step(bypresentationtime:waspinned:).md)
  Moves the cursor by a given delta time on the presentation timeline.
- [func stepInDecodeOrder(byCount: Int64) -> Int64](avsamplecursor/stepindecodeorder(bycount:).md)
  Moves the cursor a given number of samples in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursor/stepinpresentationorder(bycount:))*